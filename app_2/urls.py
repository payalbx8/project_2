from django.contrib import admin
from django.urls import path
from app_2 import views

urlpatterns = [
    path("", views.index,name='app_2'),
    path("about", views.about,name='about'),
    path("services", views.services,name='services'),
    path("contact", views.contact,name='contact'),

]