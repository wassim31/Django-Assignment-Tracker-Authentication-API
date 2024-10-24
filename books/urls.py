from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list),  # List all books or create a new book
]
