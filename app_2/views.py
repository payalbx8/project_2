from django.shortcuts import render , HttpResponse
from django.template import loader


# Create your views here.

def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def about(request):
    template2 = loader.get_template("about.html")
    return HttpResponse(template2.render())

def services(request):
    template3 = loader.get_template("service.html")
    return HttpResponse(template3.render())

def contact(request):
    template4 = loader.get_template("contact.html")
    return HttpResponse(template4.render())
