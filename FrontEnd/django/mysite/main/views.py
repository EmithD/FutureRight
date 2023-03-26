from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return render(response, "main/base.html", {})
    return new_func(response)

def about(response):
    return render(response, "main/about_us.html", {})



