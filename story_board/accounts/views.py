from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import RedirectView, FormView

# from posts.models import Author


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            # Author.objects.create(user=new_user)
            login(request, new_user)
            return redirect('stories:story_list')

    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})
