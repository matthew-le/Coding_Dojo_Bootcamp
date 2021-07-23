from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_and_reg),
    path('register', views.register),
    path('login', views.login),
    path('wishes', views.index),
    path('logout', views.logout),
    path('wishes/new', views.new_wish),
    path('wishes/make_wish', views.make_wish),
    path('wishes/<int:wish_id>/edit', views.edit_wish),
    path('wishes/<int:wish_id>/update', views.update_wish),
    path('wishes/<int:wish_id>/delete', views.delete_wish),
    path('wishes/<int:wish_id>/granted', views.grant_wish),
    path('wishes/<int:wish_id>/like', views.like),
    path('wishes/<int:wish_id>/unlike', views.unlike),
    path('wishes/stats', views.stats)
]