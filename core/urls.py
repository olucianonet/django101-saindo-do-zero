from django.urls import path
from core import views


urlpatterns = [
    path('read', views.read, name='read'),
    path('create', views.create, name='create'),
    path('details/<int:id>', views.details, name='details'),
    path('delete/<int:id>', views.delete, name='delete'),
]
