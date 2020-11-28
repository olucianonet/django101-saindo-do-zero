from django.urls import path
from core import views


urlpatterns = [
    path('read', views.read, name='read'),
]
