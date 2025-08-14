# tasks/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def register_view(request):
    """
    Handles user registration.
    If the request method is POST, it processes the form data.
    If the form is valid, it saves the user and logs them in.
    If the request is GET, it displays an empty registration form.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Account created for {user.username}!")
            return redirect('task_list') # Redirect to the task list view later
        else:
            messages.error(request, "Registration failed. Please check the form errors.")
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

def login_view(request):
    """
    Handles user login.
    If the request method is POST, it authenticates the user.
    If the user is valid, it logs them in.
    If the request is GET, it displays an empty login form.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('task_list') # Redirect to the task list view later
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})

def logout_view(request):
    """
    Handles user logout.
    This view logs out the currently authenticated user.
    """
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You have been logged out successfully.")
        return redirect('login')
    return redirect('task_list') # Redirect to a safe page if not a POST request

def placeholder_home(request):
    """
    A temporary home view for logged-in users.
    """
    return render(request, 'tasks/home.html')
