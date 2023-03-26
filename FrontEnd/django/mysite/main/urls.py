from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.index, name="index"),
    path("about_us/", views.about_us, name="about_us"),
    path("help/", views.help, name="help"),
    path("start_test/", views.start_test, name="start_test"),
    path("review_test/", views.review_test, name="review_test"),
]