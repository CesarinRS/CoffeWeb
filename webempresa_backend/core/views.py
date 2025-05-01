from django.shortcuts import render, HttpResponse

# Create your views here.

"""
Inicio: /
Historia: about-us/
Contacto: contact-us/
Visitanos: find-us/
Servicios: services/
Blog: blog/
Politicas: politics/
"""

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def store(request):
    return render(request, "core/store.html")

def contact(request):
    return render(request, "core/contact.html")

