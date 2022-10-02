from django.urls import path
from . import views

urlpatterns = [
    path('follow/<int:id>', views.follow, name='follow'),
    path('unfollow/<int:id>', views.unfollow, name='unfollow'),
    path('follow_list/<int:id>/<which>', views.follow_list, name='follow_list'),
]
