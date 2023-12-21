from django.urls import path
from .views import TodoView , TodoDetailView , UserDetailView , UserView , TaskView , TaskDetailView , PriorityView , RegisterView
from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns = [
    path('registr/', RegisterView.as_view()),
    path('login/', ObtainAuthToken.as_view()),
    path('', UserView.as_view()),
    path('<int:user_id>', UserDetailView.as_view()),
    path('todos/', TodoView.as_view()),
    path('todos/<int:todo_id>/', TodoDetailView.as_view()),
    path('todos/<int:todo_id>/tasks/', TaskView.as_view()),
    path('todos/<int:todo_id>/tasks/<int:task_id>/', TaskDetailView.as_view()),
    path('todos/<int:todo_id>/tasks/<int:task_id>/priority/', PriorityView.as_view()),
]