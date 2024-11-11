from django.urls import path
from . import views

urlpatterns = [                                                     # API endpoint
    path('books/', views.get_books, name='get_books'),              # GET all books
    path('books/<int:pk>/', views.get_book, name='get_book'),        # GET single book by ID
    path('books/add/', views.add_book, name='add_book'),             # POST add book
    path('books/update/<int:pk>/', views.update_book, name='update_book'), # PUT update book
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'), # DELETE book
]
