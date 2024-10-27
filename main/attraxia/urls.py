from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('assignments/', include('assignments.urls')),

]   