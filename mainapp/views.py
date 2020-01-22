from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'mainapp/home.html')



def about(request):
    return render(request,'mainapp/about.html')


def projects(request):
    return render(request,'mainapp/projects.html')


def contact(request):
    return render(request,'mianapp/contact.html')
    