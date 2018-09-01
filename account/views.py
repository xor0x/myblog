from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import SignUpForm
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            ctx = {
                'error':'Username or Password incorrect.'
            }
            return render(request, 'accounts/login.html', ctx)
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'accounts/signup.html')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')





def password_reset(request):
    return redirect('home')
