from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('add-event/',views.add_event,name="add-event")
]