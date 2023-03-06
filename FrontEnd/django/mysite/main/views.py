from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

def v1(response):
    return HttpResponse('<h1>v1!</h1>')

def home(response):
    return render(response, "main/home.html", {})

