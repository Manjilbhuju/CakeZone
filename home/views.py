from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    views = {}
    views['feedbacks'] = Feedback.objects.all()
    views['services'] = Service.objects.all()
    views['products'] = Product.objects.all()
    return render(request,'index.html', views)

def contact(request):
    views = {}
    views['contacts'] = Contact.objects.all()
    return render(request,'contact.html',views)

def about(request):
    views = {}
    return render(request,'about.html',views)

def menu(request):
    views = {}
    return render(request,'menu.html', views)

def service(request):
    views = {}
    return render(request,'service.html', views)

def chef(request):
    views = {}
    return render(request,'team.html', views)

def feedback(request):
    views = {}
    return render(request,'testimonial.html', views)