from distutils.command.upload import upload
import email
from operator import mod
from django.db import models
from datetime import datetime

# Create your models here.
class event(models.Model):
    e_name = models.CharField(max_length=50)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    e_date = models.DateField(auto_now_add=True)
    desc = models.TextField()
    p_limit = models.IntegerField()
    brochure = models.ImageField()
    #noti = models.ForeignKey(Notification,on_delete=models.CASCADE)
    #host = models.ForeignKey(Club,on_delete=models.CASCADE)
    #participants = models.ForeignKey(Student,on_delete=models.CASCADE)
    Venue = models.CharField(max_length=255)

    def __str__(self):
        return self.e_name

class Club(models.Model):
    c_name = models.CharField(max_length=255)
    c_about = models.TextField()
    profile_pic = models.ImageField(upload_to='club')
    #c_admin = models.ForeignKey(Student,on_delete=models.CASCADE)
    



