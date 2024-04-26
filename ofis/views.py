

from django.shortcuts import render
from django.contrib import messages

def home_view(request):
    return render(request, "index.html" )


def services_view(request):
    return render(request, "services.html")

def contact_view(request):
    return render(request, "contact.html")

def about_view(request):
    return render(request, "about.html")


def base_view(request):
    return render(request,"base.html")


def client_view(request):
    return render(request,"client.html")


def blog_view(request):
    return render(request,"blog.html")


