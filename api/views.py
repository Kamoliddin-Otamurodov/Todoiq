from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication , TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Todo , Task , Priority , User

from .serializers import TodoSerializer , TaskSerializer , PrioritySerializer , UserSerializer

class RegisterView(APIView):
    def post(self, request: Request) -> Response:
        data = request.data
        data['user'] = request.user.id

        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    authentication_classes = [BasicAuthentication , TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request) -> Response:
        customer = User.objects.all()

        serializer = UserSerializer(customer, many=True)
        
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        data = request.data
        data['user'] = request.user.id

        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    def get(self, request: Request, user_id: int) -> Response:
        customer = User.objects.get(id=user_id)

        serializer = UserSerializer(customer)
        
        return Response(serializer.data)

    def put(self, request: Request, user_id: int) -> Response:
        data = request.data

        task = User.objects.get(id=user_id)

        serializer = UserSerializer(task, data=data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request: Request, user_id: int) -> Response:
        task = User.objects.get(id=user_id)
        task.delete()

        return Response({'message': 'deleted.'})
    

class TodoView(APIView):
    authentication_classes = [BasicAuthentication , TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request) -> Response:
        tasks = request.user.todos.all()

        serializer = TodoSerializer(tasks, many=True)
        
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        data = request.data
        data['user'] = request.user.id

        serializer = TodoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailView(APIView):
    def get(self, request: Request, todo_id : int) -> Response:
        customer = Todo.objects.get(id = todo_id)

        serializer = TodoSerializer(customer)
        
        return Response(serializer.data)

    def put(self, request: Request, todo_id : int) -> Response:
        data = request.data

        task = Todo.objects.get(id = todo_id)

        serializer = TodoSerializer(task, data=data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request: Request, todo_id : int) -> Response:
        task = Todo.objects.get(id = todo_id)
        task.delete()

        return Response({'message': 'deleted.'})
    

class TaskView(APIView):
    authentication_classes = [BasicAuthentication , TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request , todo_id : int) -> Response:
        customer = Task.objects.filter(todo_id = todo_id)

        serializer = TaskSerializer(customer, many=True)
        
        return Response(serializer.data)

    def post(self, request: Request , todo_id : int) -> Response:
        data = request.data
        data['user'] = request.user.id

        serializer = TaskSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    def get(self, request: Request, user_id: int , todo_id : int , task_id : int) -> Response:
        customer = Task.objects.get(todo_id = todo_id , id=task_id)

        serializer = TaskSerializer(customer)
        
        return Response(serializer.data)

    def put(self, request: Request, user_id: int , todo_id : int , task_id : int) -> Response:
        data = request.data

        task = Task.objects.get(todo_id = todo_id , id=task_id)

        serializer = TaskSerializer(task, data=data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        
    def patch(self, request: Request, user_id: int , todo_id : int , task_id : int) -> Response:
        data = request.data

        task = Task.objects.get(todo_id = todo_id , id=task_id)

        serializer = TaskSerializer(task, data=data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request: Request, user_id: int , todo_id : int , task_id : int) -> Response:
        task = Task.objects.get(todo_id = todo_id , id=task_id)
        task.delete()

        return Response({'message': 'deleted.'})
    
    from rest_framework.views import APIView


class PriorityView(APIView):
    authentication_classes = [BasicAuthentication , TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request , user_id: int , todo_id : int , task_id : int) -> Response:
        customer = Priority.objects.filter(task_id = task_id)

        serializer = PrioritySerializer(customer, many=True)
        
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        data = request.data
        data['user'] = request.user.id

        serializer = PrioritySerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""class PublisherDetailView(APIView):
    def get(self, request: Request, pk: int) -> Response:
        customer = Publisher.objects.get(id=pk)

        serializer = PublisherSerializer(customer)
        
        return Response(serializer.data)

    def put(self, request: Request, pk: int) -> Response:
        data = request.data

        task = Publisher.objects.get(id=pk)

        serializer = PublisherSerializer(task, data=data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request: Request, pk: int) -> Response:
        task = Publisher.objects.get(id=pk)
        task.delete()

        return Response({'message': 'deleted.'})"""
