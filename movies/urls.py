from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_movie, name='add_movie'),
    path('edit/<int:pk>/', views.edit_movie, name='edit_movie'),
    path('delete/<int:pk>/', views.delete_movie, name='delete_movie'),
    path('toggle/<int:pk>/', views.toggle_watched, name='toggle_watched'),
]