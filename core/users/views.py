import email
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import is_valid_path

from users.forms import SignupForm,ClubRegForm

# Create your views here.


def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email+"   "+password)
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
            # Redirect to a success page.
        else:
            messages.success(request,"error in login")
            return redirect('login')
            # Return an 'invalid login' error message.
    else:
        return render(request, 'users/login.html', {})
def logout_user(request):
    logout(request)
    return redirect('index')        


def signup_user(request):
    form = SignupForm()
    club_form = ClubRegForm()
    context={"form":form,"club":club_form}

    if request.method=='POST' :
        form = SignupForm(request.POST)
        club_form = ClubRegForm(request.POST,request.FILES)
        if form.is_valid() and club_form.is_valid():
            #save the details
            form.save()
            club_form.save(commit=False) 
        return redirect('login')
    return render(request,'users/reg.html', context)