from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('add-event/',views.add_event,name="add-event"),
    path('club/<int:id>/event_panel/',views.edit_event,name="event_panel"),
    path('<int:id>/event/',views.event,name="event"),
    path('club/',views.club,name="club"),
    path('club-p/',views.club_p,name="club-p"),
    path('club-n/',views.club_n,name="club-n"),
    path('student/',views.student,name="student"),
    path('student-reg/',views.reg_event,name="student-reg"),
    
    
    
]