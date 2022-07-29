from dataclasses import field
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError  

from users.models import Account

class SignupForm(UserCreationForm):
    
    email = forms.EmailField(max_length=100,help_text="required field.Add a valid email address")
    class Meta:
        model = Account
        fields = ('email','username','password1','password2')

    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = Account.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = Account.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
  
    def save(self, commit = True):  
        user = Account.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1'] 
        )  
        return user      

   