from django.utils.translation import gettext as _
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.sessions.models import Session
from .models import Account
from .forms import SignupForm, StudentRegForm

# Create your views here.


def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email+"   "+password)
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('club')
            else: 
                return redirect('student')
            # Redirect to a success page.
        else:
            messages.success(request,"error in login")
            return redirect('login')
            # Return an 'invalid login' error message.
    else:
        return render(request, 'users/login.html', {})

        
@login_required
def logout_user(request):
    logout(request)
    return redirect('login')        





def signup_user(request):
    if request.method == 'POST':
        user_form = SignupForm(request.POST)
        if user_form.is_valid():
            # Save the user
            user = user_form.save()
            request.session['user_id'] = user.id
            # Redirect to the next page for student details (student_creation)
            return redirect(reverse('student_creation', kwargs={'user_id': user.id}))
    else:
        user_form = SignupForm()

    return render(request, 'users/signup_user.html', {'user_form': user_form})

def student_creation(request, user_id):
    if request.method == 'POST':
        # Handle POST request
        user = get_object_or_404(Account, id=user_id)

        student_form = StudentRegForm(request.POST, request.FILES)
        if student_form.is_valid():
            # Save the student profile
            
            print(f"---{user}")
            student = student_form.save(commit=False)
            student.user = user
            student.save()

            # Clear the user ID from the session
            if 'user_id' in request.session:
                del request.session['user_id']

            return redirect('login')  # Redirect to login or another page
    else:
        # Handle GET request
        # Check if the user ID is in the session
        user_id_from_session = request.session.get('user_id')

        if not user_id_from_session:
            return redirect('signup_user')  # Redirect to signup_user if user_id is not in session

        user = get_object_or_404(Account, id=user_id_from_session)
        student_form = StudentRegForm(request.POST, request.FILES)
        
        return render(request, 'users/student_creation.html', {'student_form': student_form,'user_id':user.id})
