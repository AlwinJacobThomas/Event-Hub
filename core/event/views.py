
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    events=[
        {
            'title':"paradox",
            'club':"IEEE",
            'type':"Tech Fest"
        },
        {
            'title':"Lumere",
            'club':"UNION",
            'type':"National Tech and Cultural Fest"
        },
        {
            'title':"Confictura",
            'club':"Ajagajans",
            'type':"department fest"
        }
    ]
    return render(request,'index.html',{"events":events})