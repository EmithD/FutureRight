from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("v1/", views.v1, name="view 1"),
    path("home/", views.home, name="home")
]