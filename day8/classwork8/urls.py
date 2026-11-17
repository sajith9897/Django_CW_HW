from django.urls import path
from classwork8 import views

app_name = 'classwork8'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]