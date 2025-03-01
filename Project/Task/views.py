from django.template.defaultfilters import title
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from Task.serializers import TaskSerializer
from Task.models import Task


class TaskListCreatAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        completed = serializer.validated_data.get('completed')
        created = serializer.validated_data.get('created')
        task = Task.objects.create(
            title=title,
            description=description,
            completed=completed,
            created_at=created_at
        )
        task.save()
        return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)


class TaskDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        task_detail = self.get_object()
        serializer = TaskSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        task_detail.title = serializer.validated_data.get('title')
        task_detail.description = serializer.validated_data.get('description')
        task_detail.completed = serializer.validated_data.get('completed')
        task_detail.created_at = serializer.validated_data.get('created_at')
        task_detail.save()
        return Response(TaskSerializer(task_detail).data, status=status.HTTP_200_OK)
