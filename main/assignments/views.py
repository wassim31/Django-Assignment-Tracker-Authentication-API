from rest_framework import viewsets, generics, permissions, filters
from .models import Assignment, AssignmentStatusLog
from .serializers import AssignmentSerializer, AssignmentStatusLogSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json

def broadcast_assignment_update(instance):
    channel_layer = get_channel_layer()
    data = AssignmentSerializer(instance).data
    async_to_sync(channel_layer.group_send)(
        'assignment_updates', 
        {'type': 'send_assignment_update', 'data': json.dumps(data)}
    )

class AssignmentPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    
class AssignmentListCreateView(generics.ListCreateAPIView):
    queryset = Assignment.objects.all().order_by('-created_at')
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'assignee']
    search_fields = ['name', 'description']
    ordering_fields = ['created_at', 'updated_at']
    pagination_class = AssignmentPagination

    def perform_create(self, serializer):
        serializer.save()
        broadcast_assignment_update(instance)


class AssignmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        instance = self.get_object()
        old_status = instance.status
        instance = serializer.save()
        new_status = instance.status
        broadcast_assignment_update(instance)

        if old_status != new_status:
            AssignmentStatusLog.objects.create(
                assignment=instance,
                old_status=old_status,
                new_status=new_status
            )

        broadcast_assignment_update(instance)
    
class AssignmentStatusLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AssignmentStatusLog.objects.all()
    serializer_class = AssignmentStatusLogSerializer
