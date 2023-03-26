from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.index, name="index"),
    path("about_us/", views.about_us, name="about_us"),
]