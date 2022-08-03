from django import forms
from django.forms import ModelForm
from .models import Event

class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('e_name','e_date','desc','p_limit','brochure','e_type','reg_fee')

    def __init__(self, *args, **kwargs):   
        super().__init__(*args, **kwargs)
        self.fields['e_name'].widget.attrs.update({"class":"bg-red-300 w-full "})
        self.fields['e_date'].widget.attrs.update({"class":"bg-green-300 w-full"})
        self.fields['desc'].widget.attrs.update({"class":"bg-green-300 w-full h-28"})
        self.fields['p_limit'].widget.attrs.update({"class":"bg-green-300 w-full"})
        self.fields['brochure'].widget.attrs.update({"class":"bg-green-300 w-full"})
        self.fields['e_type'].widget.attrs.update({"class":"bg-green-300 w-full"})
        self.fields['reg_fee'].widget.attrs.update({"class":"bg-green-300 w-full"})

class EventRegForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ()
     