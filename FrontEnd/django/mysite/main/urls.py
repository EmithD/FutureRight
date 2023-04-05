from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.index, name="home"),
    path("about_us/", views.about_us, name="about_us"),
    path("help/", views.help, name="help"),
    path("start_test/", views.start_test, name="start_test"),
    path("review_test/", views.review_test, name="review_test"),
    path("test/", views.test, name="test"),
    path("therm_use/", views.therm_use, name="therm_use"),
]
