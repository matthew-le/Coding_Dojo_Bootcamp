from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.book),
    path('authors', views.author),
    path('add_author', views.add_author),
    path('add_book', views.add_book),
    path('books/<int:book_id>', views.book_info),
    path('authors/<int:author_id>', views.author_info),
    path('books/<int:book_id>/process_new_author', views.process_new_author),
    path('authors/<int:author_id>/process_new_book', views.process_new_book)

]