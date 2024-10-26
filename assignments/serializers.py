from rest_framework import serializers
from .models import Assignment, AssignmentStatusLog

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'name', 'description', 'assignee', 'status', 'created_at', 'updated_at']

class AssignmentStatusLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentStatusLog
        fields = ['id', 'assignment', 'status', 'timestamp']
