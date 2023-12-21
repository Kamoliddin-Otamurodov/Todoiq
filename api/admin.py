from django.contrib import admin
from .models import Todo , Task , Priority

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'created_at']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'todo', 'title', 'description', 'status' , 'created_at' , 'due_date']


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ['id', 'task_id', 'name']

