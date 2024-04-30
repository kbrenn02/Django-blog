from django.http import HttpResponse;
from django.shortcuts import render; # to render templates, you need to import the render module

def homepage(request):
    # return HttpResponse('homepage')
    return render(request,'homepage.html')
    

def about(request):
    # return HttpResponse('about')
    return render(request,'about.html')