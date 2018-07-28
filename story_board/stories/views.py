from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, FormView

# from rest_framework import generics
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response

from .forms import Story_Form
from .models import Story


User = get_user_model()


def get_request_user(self):
    request_user = self.request.user
    request_user, created = User.objects.get_or_create(
        username=request_author_user.username)
    return request_author


def story_form(self, request):
    form = self.form_class(request.POST)
    try:
        request_user = get_request_user(self)
    except Exception:
        request_user = self.request.user
    else:
        pass
    if form.is_valid():
        if "post" in self.request.POST:
            post = form.save(commit=False)
            if self.request.user.is_authenticated:
                post.author = request_user
            else:
                pass
            post.save()


def story_recommend(self, request):
    if 'recommend' or 'unrecommend' in self.request.POST:
        request_user = get_request_user(self)
        if 'recommend' in self.request.POST:
            story_id = request.POST.get('recommend')
            story = get_object_or_404(Story, id=story_id)
            story.recommendations.add(request_user)
        elif 'unrecommend' in self.request.POST:
            story_id = request.POST.get('unrecommend')
            story = get_object_or_404(Story, id=story_id)
            story.recommendations.remove(request_user)


def follow_user(self, request):
    if 'follow' or 'unfollow' in self.request.POST:
            request_user = get_request_user(self)
            target_user = User.objects.get(username=self.kwargs['user'])
            if 'follow' in self.request.POST:
                request_user.following.add(target_user)
                target_user.followers.add(self.request.user)
            elif 'unfollow' in self.request.POST:
                request_user.following.remove(target_user)
                target_user.followers.remove(self.request.user)
            return target_user


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
            context['guest_user'] = User.objects.get(
                username=self.request.user.username)
        return context

    def post(self, request, *args, **kwargs):
        story_form(self, request)
        try:
            story_recommend(self, request)
        except Exception:
            pass
        finally:
            return HttpResponseRedirect(Story.get_absolute_url(self))


# class User_Post_List(ListView, FormView):
#     context_object_name = 'posts'
#     model = Post
#     form_class = Post_Form
#     template_name = 'posts/user_post_list.html'

#     def get_queryset(self):
#         author_username = self.kwargs['author']
#         user = get_object_or_404(User, username=author_username)
#         author = get_object_or_404(Author, user=user)
#         return self.model.objects.filter(author=author).order_by('-id')

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         host_author = self.kwargs['author']
#         context['host_author'] = host_author
#         context['host_author_user'] = User.objects.get(
#             username=host_author)
#         if self.request.user.is_authenticated:
#             context['guest_author'] = Author.objects.get(
#                 user=self.request.user)
#         return context

#     def post(self, request, *args, **kwargs):
#         post_form(self, request)
#         post_recommend(self, request)
#         target_author = post_follow(self, request,)
#         return redirect('posts:user_post_list', author=target_author)


# class Following_Post_List(ListView, FormView):
#     context_object_name = 'posts'
#     model = Post
#     form_class = Post_Form
#     template_name = 'posts/post_list.html'

#     def get_queryset(self):
#         guest_author = get_object_or_404(Author, user=self.request.user)
#         followee_list = []
#         for followee in guest_author.following.all():
#             followee_list.append(followee.author)
#         return self.model.objects.filter(
#             author__in=followee_list).order_by('-id')

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         if self.request.user.is_authenticated:
#             context['guest_author'] = Author.objects.get(
#                 user=self.request.user)
#         return context

#     def post(self, request, *args, **kwargs):
#         post_form(self, request)
#         post_recommend(self, request)
#         return HttpResponseRedirect(Post.get_absolute_url(self))