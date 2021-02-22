from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'first_app/index.html')

def filter(request):
    return render(request,'first_app/filter.html')

def movie1(request):
    return render(request,'first_app/movie1.html')
