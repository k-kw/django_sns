from django.urls import path
from . import views

urlpatterns = [
    path('senddm/<int:id>', views.senddm, name='senddm'),
    path('alldm/<int:id>', views.alldm, name='alldm'),
]
