from django.db import models
from accounts.models import CustomUserManager as User

class Assignment(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('error', 'Error'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    #assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class AssignmentStatusLog(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Assignment.STATUS_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['timestamp']),
        ]
