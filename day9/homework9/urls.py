
from django.urls import path
from . import views

app_name = 'homework9'

urlpatterns = [
    path('', views.home, name='home'),
]
