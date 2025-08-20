# tasks/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Task
from .forms import TaskForm

# --- Authentication Views  ---
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Account created for {user.username}!")
            return redirect('task_list')
        else:
            messages.error(request, "Registration failed. Please check the form errors.")
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('task_list')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You have been logged out successfully.")
        return redirect('login')
    return redirect('task_list')

# --- Task Management Views ---

class TaskListView(LoginRequiredMixin, ListView):
    """
    View to display a list of tasks for the logged-in user.
    """
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        """
        Returns only the tasks that belong to the current logged-in user.
        """
        return self.request.user.tasks.all().order_by('-created_at')

class TaskCreateView(LoginRequiredMixin, CreateView):
    """
    View to handle the creation of a new task.
    """
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        """
        This method is called when the form is valid.
        It automatically assigns the logged-in user as the task owner before saving.
        """
        form.instance.user = self.request.user
        messages.success(self.request, "Task created successfully!")
        return super().form_valid(form)

class TaskDetailView(LoginRequiredMixin, DetailView):
    """
    View to display the details of a single task.
    """
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

    def get_queryset(self):
        """
        Ensures the user can only view tasks they own.
        """
        return self.request.user.tasks.all()


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """
    View to handle the updating of an existing task.
    """
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        """
        Ensures the user can only update tasks they own.
        """
        return self.request.user.tasks.all()

    def form_valid(self, form):
        """
        Adds a success message after a task is updated.
        """
        messages.success(self.request, "Task updated successfully!")
        return super().form_valid(form)

