
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import  Event

# Create your views here.

def index(request):
    events=Event.objects.all()
    
    if request.user.is_authenticated:
        user =request.user
        content= {
                    "user":user,
                    "events":events
        }
    else:
        content ={}           
    return render(request,'index.html',content)