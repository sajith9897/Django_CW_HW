from homework1 import views
from django.urls import path

urlpatterns = [
  path('for gallery', views.gallery),
  path('for contact', views.contact)
]