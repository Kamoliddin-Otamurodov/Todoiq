from rest_framework import serializers
from .models import Todo , Task , Priority , User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class PrioritySerializer(serializers.ModelSerializer):

    class Meta:
        model = Priority
        fields = '__all__'