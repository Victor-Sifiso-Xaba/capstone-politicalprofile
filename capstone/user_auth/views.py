from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, UserProfileForm
from django.contrib import messages


def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('polls:index')  # Redirect to polls:index after registration
    else:
        form = CustomUserCreationForm()

    return render(request, 'user_auth/register_user.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('polls:index')  # Redirect to polls:index after registration
    else:
        form = CustomUserCreationForm()

    return render(request, 'user_auth/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Use Django's built-in authentication to log in the user
            user = form.get_user()
            login(request, user)
            return redirect('polls:index')  # Redirect to polls:index after login
    else:
        form = AuthenticationForm()

    return render(request, 'user_auth/login_user.html', {'form': form})

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You have been successfully logged out.")
        return redirect('polls:index')  # Redirect to the polls index or any other desired page

    # If it's a GET request, just render the logout page
    return render(request, 'user_auth/templates/user_auth/logout_user.html')
