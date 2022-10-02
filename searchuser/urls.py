from django.urls import path
from .views import UserListView
from . import views

urlpatterns=[
    path('userlist/', UserListView.as_view(), name='userlist'),
    path('publicprofile/<int:prfid>', views.publicprofile, name='publicprofile'),
    path('searchusers', views.searchusers, name='searchusers'),
]