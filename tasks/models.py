# tasks/models.py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    """
    Represents a single task for a user.
    """
    # The title of the task (required)
    title = models.CharField(max_length=200)

    # An optional detailed description of the task
    description = models.TextField(blank=True, null=True)

    # An optional due date for the task
    due_date = models.DateField(blank=True, null=True)

    # A boolean field to track if the task is completed
    completed = models.BooleanField(default=False)

    # Automatically sets the creation date when the task is created
    created_at = models.DateTimeField(auto_now_add=True)

    # A ForeignKey to the User model, linking each task to a user
    # on_delete=models.CASCADE means if a User is deleted, all their tasks are also deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        """
        String representation of the Task model, useful for the admin site.
        """
        return self.title

