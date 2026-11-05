from homework3 import views
from django.urls import path

urlpatterns = [
  path('', views.list),
]