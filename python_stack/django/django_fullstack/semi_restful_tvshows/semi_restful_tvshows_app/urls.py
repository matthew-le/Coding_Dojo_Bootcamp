from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.show),
    path('shows/new', views.add_show),
    path('shows/create_show', views.create_show),
    path('shows/<int:show_id>', views.show_info),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('shows/<int:show_id>/update', views.update_show),
    path('shows/<int:show_id>/delete', views.delete_show)
]
