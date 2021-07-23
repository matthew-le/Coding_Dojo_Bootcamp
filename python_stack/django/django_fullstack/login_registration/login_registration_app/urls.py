from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_register),
    path('register', views.register),
    path('login', views.login),
    path('index', views.index),
    path('logout', views.logout),
]
