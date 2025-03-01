from rest_framework import serializers
from Task.models import Task

class TaskSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    completed = serializers.BooleanField()
    created = serializers.DateTimeField()