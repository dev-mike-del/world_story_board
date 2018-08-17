from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, FormView, DetailView, UpdateView

from .forms import Story_Form
from .models import Author, Story


User = get_user_model()


def get_request_author(self):
    request_author_user = self.request.user
    request_author, created = Author.objects.get_or_create(
        user=request_author_user)
    return request_author


def story_form(self, request):
    form = self.form_class(request.POST)
    try:
        request_author = get_request_author(self)
    except Exception:
        request_author = self.request.user
    else:
        pass
    if form.is_valid():
        if "publish" in self.request.POST:
            story = form.save(commit=False)
            if self.request.user.is_authenticated:
                story.author = request_author
            else:
                pass
            story.save()


def story_recall_and_republish(self, request):
    if 'recall' in self.request.POST:
        story_id = request.POST.get('recall')
        story = get_object_or_404(Story, id=story_id)
        story.published = False
        story.save()
    if 'republish' in self.request.POST:
        story_id = request.POST.get('republish')
        story = get_object_or_404(Story, id=story_id)
        story.published = True
        story.save()


def story_recommend(self, request):
    if 'recommend' or 'unrecommend' in self.request.POST:
        request_author = get_request_author(self)
        if 'recommend' in self.request.POST:
            story_id = request.POST.get('recommend')
            story = get_object_or_404(Story, id=story_id)
            story.recommendations.add(request_author)
        elif 'unrecommend' in self.request.POST:
            story_id = request.POST.get('unrecommend')
            story = get_object_or_404(Story, id=story_id)
            story.recommendations.remove(request_author)


def author_follow(self, request):
    if 'follow' or 'unfollow' in self.request.POST:
        request_author = get_request_author(self)
        target_author_str = self.kwargs['author_slug']
        target_author_user = User.objects.get(username=target_author_str)
        target_author, created2 = Author.objects.get_or_create(
            user=target_author_user)
        if 'follow' in self.request.POST:
            request_author.following.add(target_author_user)
            target_author.followers.add(self.request.user)
        elif 'unfollow' in self.request.POST:
            request_author.following.remove(target_author_user)
            target_author.followers.remove(self.request.user)
        return target_author


def About(request):
    return render(request, 'stories/about.html')

class Story_List(ListView, FormView):
    context_object_name = 'stories'
    model = Story
    form_class = Story_Form
    template_name = 'stories/story_list.html'

    def get_queryset(self):
        return self.model.objects.filter(published=True).order_by('-id')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            try:
                context['guest_author'] = Author.objects.get(
                    user=self.request.user)
            except Exception:
                pass
            
        return context

    def post(self, request, *args, **kwargs):
        story_form(self, request)
        try:
            story_recommend(self, request)
        except Exception:
            pass
        try:
            story_recall_and_republish(self,request)
        except Exception:
            pass
        return HttpResponseRedirect(Story.get_absolute_url(self))

class Author_Story_List(DetailView, UpdateView, FormView):
    context_object_name = 'author'
    model = Author
    slug_field = 'author_slug'
    slug_url_kwarg = 'author_slug'
    form_class = Story_Form
    template_name = 'stories/author_story_list.html'

    def get_queryset(self):
        try:
            return self.model.objects.filter(
                author_slug=self.kwargs['author_slug'])
        except Exception:
            pass
        else:
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            host_author_user = User.objects.get(username=kwargs['object'])
            host_author = Author.objects.get(user=host_author_user)

            if self.request.user == host_author_user:
                context['stories'] = Story.objects.filter(author=host_author).all().order_by('-id')
            else:
                context['stories'] = Story.objects.filter(
                    Q(author=kwargs['object']),
                    Q(published=True)).all().order_by('-id')

            context['author'] = host_author

            context['guest_author'] = Author.objects.get(
                user=self.request.user)

        except Exception:
            pass
        return context

    def post(self, request, *args, **kwargs):
        story_form(self, request)
        try:
            story_recommend(self, request)
        except Exception:
            pass
        try:
            story_recall_and_republish(self,request)
        except Exception:
            pass
        target_author = author_follow(self, request,)
        return redirect('stories:author_story_list', author_slug=target_author)


class Author_Story_Update(UpdateView):
    context_object_name = 'story'
    model = Story
    slug_field = 'story_slug'
    slug_url_kwarg = 'story_slug'
    form_class = Story_Form
    template_name = 'stories/author_story_update.html'


class Following_Story_List(ListView, FormView):
    context_object_name = 'stories'
    model = Story
    form_class = Story_Form
    template_name = 'stories/story_list.html'

    def get_queryset(self):
        guest_author = get_object_or_404(Author, user=self.request.user)
        followee_list = []
        for followee in guest_author.following.all():
            followee_list.append(followee.author)
        return self.model.objects.filter(
            author__in=followee_list).order_by('-id')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['guest_author'] = Author.objects.get(
                user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        story_form(self, request)
        story_recommend(self, request)
        return HttpResponseRedirect(Story.get_absolute_url(self))



