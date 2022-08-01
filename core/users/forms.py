
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model #global user from settings.py

User=get_user_model()
# from django.contrib.auth import authenticate
# from django.core.exceptions import ValidationError  

from users.models import Account

class SignupForm(UserCreationForm):
    
    
    def __init__(self, *args, **kwargs):   
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({"class":"bg-red-300 w-full"})
        self.fields['username'].widget.attrs.update({"class":"bg-blue-300 w-full"})
        self.fields['password1'].widget.attrs.update({"class":"bg-green-300 w-full"})
        self.fields['password2'].widget.attrs.update({"class":"bg-yellow-300 w-full"})
        #self.fields['profile_image'].widget.attrs.update({"class":"bg-red-300"})
    class Meta:
        model = User #user in settings.py -Account
        fields = ('email','username','password1','password2')

    # def username_clean(self):  
    #     username = self.cleaned_data['username'].lower()  
    #     new = Account.objects.filter(username = username)  
    #     if new.count():  
    #         raise ValidationError("User Already Exist")  
    #     return username  
  
    # def email_clean(self):  
    #     email = self.cleaned_data['email'].lower()  
    #     new = Account.objects.filter(email=email)  
    #     if new.count():  
    #         raise ValidationError(" Email Already Exist")  
    #     return email  
  
    # def clean_password2(self):  
    #     password1 = self.cleaned_data['password1']  
    #     password2 = self.cleaned_data['password2']  
  
    #     if password1 and password2 and password1 != password2:  
    #         raise ValidationError("Password don't match")  
    #     return password2 


   