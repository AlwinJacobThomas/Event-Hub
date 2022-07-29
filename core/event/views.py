
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import  Event

# Create your views here.

def index(request):
    events=Event.objects.all()
    user =request.user
    a = False
    return render(request,'index.html',{"events":events,"admin":a,"user":user})