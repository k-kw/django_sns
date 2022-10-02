from django.urls import path
from . import views

urlpatterns = [
    path('yourprofile/', views.yourprofile, name='yourprofile'),
    path('upprofile/', views.upprofile, name='upprofile'),
    path('set_default/', views.set_default, name='set_default'),
    path('editprofile/', views.editprofile, name='editprofile'),
]
