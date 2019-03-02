from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from rest_framework.authtoken.models import Token

from stories.models import Author


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            Author.objects.create(user=new_user)
            login(request, new_user)
            return redirect('stories:story_list')

    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def api_token_register(request):
    if request.method == 'POST':

        author = get_object_or_404(Author, user=request.user)
        Token.objects.get_or_create(user=request.user)

        return HttpResponseRedirect(
            reverse(
                'stories:author_story_list',
                kwargs={'author_slug': author.author_slug},
            )
        )
    return render(request, 'accounts/api_token_auth.html',)



