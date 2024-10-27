from django.urls import path, include

urlpatterns = [
    path('user/', include('user_authentification.urls')),  # Include the app's URLs
    path('api/assignments', include('assignments.urls')),

]