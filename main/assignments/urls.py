from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'assignment-status-logs', views.AssignmentStatusLogViewSet, basename='assignment-status-log')

urlpatterns = [
    path('assignments/', views.AssignmentListCreateView.as_view(), name='assignment-list-create'),
    path('assignments/<int:pk>/', views.AssignmentDetailView.as_view(), name='assignment-detail'),
    path('', include(router.urls)),  # Include the router's URLs
]
