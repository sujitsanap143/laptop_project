from django.urls import path

from . import views

urlpatterns = [
    path('suv/', views.sign_up_view, name = 'signup_url'),
    path('siv/', views.sign_in_view, name = 'signin_url'),
    path('sov/', views.sign_out_view, name = 'signout_url')
]