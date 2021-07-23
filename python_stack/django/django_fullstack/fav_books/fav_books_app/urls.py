from django.urls import path
from . import views 

urlpatterns = [
    path('', views.log_and_reg),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('books', views.books),
    path('add_book', views.add_book),
    path('books/<int:book_id>/edit', views.edit_book),
    path('books/<int:book_id>/update', views.update_book),
    path('books/<int:book_id>/delete', views.delete_book),
    path('books/<int:book_id>/favorite', views.favorite),
    path('books/<int:book_id>/unfavorite', views.unfavorite)
]
