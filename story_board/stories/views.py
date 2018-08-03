from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, FormView, DetailView

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


def story_recommend(self, request):
    print("in story_recommed")
    print(self.request.POST)
    if 'recommend' or 'unrecommend' in self.request.POST:
        request_author = get_request_author(self)
        print(request_author)
        if 'recommend' in self.request.POST:
            story_id = request.POST.get('recommend')
            print(story_id)
            story = get_object_or_404(Story, id=story_id)
            print(story)
            story.recommendations.add(request_author)
        elif 'unrecommend' in self.request.POST:
            story_id = request.POST.get('unrecommend')
            story = get_object_or_404(Story, id=story_id)
            story.recommendations.remove(request_author)


def story_follow(self, request):
    if 'follow' or 'unfollow' in self.request.POST:
            request_author = get_request_author(self)
            target_author_str = self.kwargs['author']
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


class Story_List(ListView, FormView):
    context_object_name = 'stories'
    model = Story
    form_class = Story_Form
    template_name = 'stories/story_list.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

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
        finally:
            return HttpResponseRedirect(Story.get_absolute_url(self))

class Author_Story_List(DetailView):
    context_object_name = 'author'
    model = Author
    slug_field = 'author_slug'
    slug_url_kwarg = 'author_slug'
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
            context['stories'] = Story.objects.filter(
                author=kwargs['object'])
            context['author'] = Author.objects.get(
                user=kwargs['object'])
            context['guest_author'] = Author.objects.get(
                user=self.request.user)
        except Exception:
            pass
        return context

