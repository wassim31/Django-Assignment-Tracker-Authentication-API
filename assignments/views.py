from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Assignment, AssignmentStatusLog
from .serializers import AssignmentSerializer, AssignmentStatusLogSerializer
from django.utils import timezone
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    def update(self, request, *args, **kwargs):
        assignment = self.get_object()
        old_status = assignment.status
        response = super().update(request, *args, **kwargs)

        new_status = request.data.get('status')
        if new_status and new_status != old_status:
            AssignmentStatusLog.objects.create(
                assignment=assignment,
                status=new_status,
                timestamp=timezone.now()
            )

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'assignments',  
                {
                    'type': 'status_update',
                    'message': {
                        'assignment_id': assignment.id,
                        'new_status': new_status,
                        'timestamp': timezone.now().isoformat(),
                    }
                }
            )

        return response

class AssignmentStatusLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AssignmentStatusLog.objects.all()
    serializer_class = AssignmentStatusLogSerializer
