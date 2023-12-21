from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='todos')
    title = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"
    

class Task(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE , related_name='tasks')
    title = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    

class Priority(models.Model):
    choices = [
        ('Must do', 'Must do'),
        ('Should do', 'Should do'),
        ('Nice to do', 'Nice to do'),
        ('Delegate', 'Delegate'),
        ('Eliminate', 'Eliminate'),
    ]
    name = models.CharField(max_length=20, unique=True, choices=choices)
    task_id = models.OneToOneField(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.name