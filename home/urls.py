from .views import *
from django.urls import path

urlpatterns = [
    path("", home,name = "home"),
    path("contact", contact, name="contact"),
    path("about", about, name="about"),
    path("menu", menu, name="menu"),
    path("service", service, name="service"),
    path("chef", chef, name="team"),
    path("feedback", feedback, name="testimonial"),
]