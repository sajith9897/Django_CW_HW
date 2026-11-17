
from django.urls import path
from . import views

app_name = "classwork9"

urlpatterns = [
    path("", views.home, name="home"),
    path("login/<str:name>/", views.login_page, name="login"),
    path("result/<str:name>/", views.result, name="result"),
]
