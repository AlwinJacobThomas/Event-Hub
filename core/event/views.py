
from importlib.resources import contents
from unicodedata import name
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import  Event
from .forms import AddEventForm
# Create your views here.

def index(request):
    events=Event.objects.all()
    
    if request.user.is_authenticated:
        user =request.user
        events = Event.objects.all()
        content= {  "events":events,
                    "user":user,
                    "events":events
        }
        return render(request,'club/dashboard.html', content)
    else:
        content ={}           
    return render(request,'index.html',content)

def add_event(request):
    form = AddEventForm()
    
    context={"form":form}

    if request.method=='POST' :
        form = AddEventForm(request.POST,request.FILES)
        
        if form.is_valid():
            #save the details
            form.save() 
        return redirect('index')
    return render(request,'club/add-event.html', context)
def event(request,id):
    
    event = Event.objects.get(pk=id)
    
    content ={"event":event}
    return render(request,'event.html', content)
    
    