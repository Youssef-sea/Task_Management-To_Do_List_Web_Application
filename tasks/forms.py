# tasks/forms.py

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    """
    A ModelForm for creating and updating Task objects.
    It automatically handles validation based on the Task model fields.
    """
    class Meta:
        # Link this form to the Task model
        model = Task
        # Specify the fields that should appear in the form
        fields = ['title', 'description', 'due_date', 'completed']



