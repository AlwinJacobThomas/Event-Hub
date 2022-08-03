
from importlib.resources import contents
from unicodedata import name
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse

from users.models import Student, Club
from .models import  Event
from django.contrib.auth.decorators import login_required
from .forms import AddEventForm, EventRegForm
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    if request.user.is_authenticated:        
        return redirect('student')
    else:
        events=Event.objects.all()
        return render(request,'index.html',{'events':events})
# -----------club-------------------------
@login_required
def club(request):
    user =request.user
    student = Student.objects.get(user=user)
    try:
        club = Club.objects.get(user=student)
        events = Event.objects.filter(club=club)
        content= {  "events":events,
                    "user":user,
        }
        return render(request,'club/club-dash.html', content)
    except ObjectDoesNotExist:
        content ={}   
        return redirect('student')
@login_required
def club_p(request):
    user =request.user
    student = Student.objects.get(user=user)
    try:
        club = Club.objects.get(user=student)
        events = Event.objects.filter(attendees=student)
        content= {  "events":events,
                    "user":user,
        }
        return render(request,'club/club-dash-p.html', content)
    except ObjectDoesNotExist:
        content ={}   
        return redirect('student')
@login_required
def club_n(request):
    user =request.user
    student = Student.objects.get(user=user)
    try:
        club = Club.objects.get(user=student)
        events = Event.objects.all()
        content= {  "events":events,
                    "user":user,
        }
        return render(request,'club/club-dash-n.html', content)
    except ObjectDoesNotExist:
        content ={}   
        return redirect('student')  

#------------end club--------------------------
#----------------student----------------------
@login_required
def student(request):
    user =request.user
    student = Student.objects.get(user=user)
    try:
        club = Club.objects.get(user=student)
        return redirect('club')
    except ObjectDoesNotExist:
        new_events = Event.objects.exclude(attendees=student)
        content= {  "new_events":new_events,
                    "user":user,
        }
        return render(request,'student-dash.html', content)
#----------------end student----------------
#----------------event----------------------
@login_required
def reg_event(request):
    user =request.user
    student = Student.objects.get(user=user)
    reg_events = Event.objects.filter(attendees=student)
    content= {  "reg_events":reg_events,
                "user":request.user,
    }
    return render(request,'student-dash2.html', content)    
@login_required
def add_event(request):
    form = AddEventForm()
    
    context={"form":form}
    user =request.user
    student = Student.objects.get(user=user)
    try:
        if request.method=='POST' :
            club = Club.objects.get(user=student)
            form = AddEventForm(request.POST,request.FILES)
            if form.is_valid():
                #save the details
                post=form.save(commit=False)
                post.club=club
                post.save()
            return redirect('club')
        return render(request,'club/add-event.html', context)
    except ObjectDoesNotExist:
        return redirect('index')

def event(request,id):
    event = Event.objects.get(pk=id)
    if request.user.is_authenticated:
        user =request.user
        student = Student.objects.get(user=user)
        try:
            instance = Event.objects.get(pk=id, attendees=student)
            if request.method == 'POST':
                form = EventRegForm(request.POST, instance=instance)
                if form.is_valid():
                    post=form.save(commit=False)
                    post.attendees.remove(student)
                    post.save()
                    return redirect('student-reg')
                else:
                    return HttpResponse('error')
            return render(request, 'event.html', {
                    'event': event,
                    'enrolled': True
                })
        except ObjectDoesNotExist:
            instance = Event.objects.get(pk=id)
            if request.method == 'POST':
                form = EventRegForm(request.POST, instance=instance)
                if form.is_valid():
                    post=form.save(commit=False)
                    post.attendees.add(student)
                    post.save()
                    return redirect('student-reg')
                else:
                    return HttpResponse('error')
            return render(request, 'event.html', {
                    'event': event,
                    'enrolled': False
                })
def edit_event(request,id):
    student = Student.objects.get(user=request.user)
    club = Club.objects.get(user=student)
    event = Event.objects.get(pk=id,club=club)
    if request.user.is_authenticated:
        user =request.user
        student = Student.objects.get(user=user)
        try:
            instance = Event.objects.get(pk=id,club=club)
            if request.method == 'POST':
                form = EventRegForm(request.POST or None, instance=instance)
                if form.is_valid():
                    post=form.save(commit=False)
                    post.attendees.remove(student)
                    post.save()
                    return redirect('club')
                else:
                    return HttpResponse('error')
            return render(request,'club/event-panel.html', {
                    'event': event,
                    
                })
        except ObjectDoesNotExist:
                return redirect('club')
#----------------end event--------------------------    