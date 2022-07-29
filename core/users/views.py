import email
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import is_valid_path
from users.forms import SignupForm

# Create your views here.


def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)
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
def signup_user(request,*args,**kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"you are  already logged in as { user.email }")
    context={

    }
    if request.POST :
        form = SignupForm(request.POST)
        if form.is_valid():
            #save the details
            form.save() 
            email = form.cleaned_data.get('email').lower() 
            #authenticating with the credentials
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email,password=raw_password)
            login(request,account)
            destination = kwargs.get('next')
            if destination:
                return redirect(destination)
            return redirect("index")

        else:
            context['signup_form'] = form    
    return render(request,'users/signup.html', context)