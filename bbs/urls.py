from django.urls import path
from .views import PostmsgListView
from . import views

urlpatterns = [
    path('postmsgc/', views.postmsgc, name='postmsgc'),
    path('searchbbs/', views.searchbbs, name='searchbbs'),
    path('bbsall/', PostmsgListView.as_view(), name='bbsall'),
    path('postmsgre/<int:id>', views.postmsgre, name='postmsgre'),
]
