from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.AssignmentViewSet)
router.register(r'logs', views.AssignmentStatusLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
