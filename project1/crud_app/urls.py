from django.urls import path

from .views import laptop_create_view, laptop_retrive_view, laptop_update_view, laptop_delete_view

urlpatterns = [
    path('lcv/', laptop_create_view, name ='add_url'),
    path('lrv/', laptop_retrive_view, name = 'show_url'),
    path('luv/<int:pk>/', laptop_update_view, name = 'update_url'),
    path('ldv/<int:pk>/', laptop_delete_view, name = 'delete_url')
]