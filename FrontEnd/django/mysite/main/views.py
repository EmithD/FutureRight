from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return render(response, "main/base.html", {})
def about_us(response):
    return render(response, "main/about_us.html", {})
def help(response):
    return render(response, "main/help.html", {})
def start_test(response):
    return render(response, "main/start_test.html", {})
def review_test(response):
    return render(response, "main/review_test.html", {})


