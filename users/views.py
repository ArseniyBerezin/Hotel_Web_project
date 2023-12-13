from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth
from django.urls import reverse


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'users/profile.html', context)


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()

    context = {
        'form': form
    }
    return render(request, 'registration/login.html', context)


def registration_view(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'registration/registration.html', context)


