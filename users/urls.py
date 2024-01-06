from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('signup_user/', views.signup_user, name='signup_user'),
    path('student_creation/<int:user_id>/', views.student_creation, name='student_creation'),
    path('logout/', views.logout_user, name="logout"),
]