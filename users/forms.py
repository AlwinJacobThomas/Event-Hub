# users/forms.py
from django import forms
from .models import Account, Student

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password']

class StudentRegForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['dept', 'year_of_passout', 'profile_pic']
