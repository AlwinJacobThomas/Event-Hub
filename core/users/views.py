from django.utils.translation import gettext as _
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import is_valid_path

from users.forms import SignupForm,StudentRegForm

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
    student_form = StudentRegForm()
    context={"form":form,"student":student_form}

    if request.method=='POST' :
        form = SignupForm(request.POST, instance=request.user)
        club_form = StudentRegForm(request.POST,request.FILES,instance=request.user.student)
        if form.is_valid() and student_form.is_valid():
            #save the details
            form.save()
            student_form.save() 
            messages.success(request,_('Your profile was successfully updated!'))
        return redirect('login')
    return render(request,'users/reg.html', context)