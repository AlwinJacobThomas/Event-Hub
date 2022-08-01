from django.db import models
import os
from django.utils.deconstruct import deconstructible
import uuid

@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid.uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join('event', filename)

path_and_rename = PathAndRename("event/")

class Event(models.Model):
    e_name = models.CharField('Event Name',max_length=50)
    date_of_creation = models.DateTimeField('Date of Creation',auto_now_add=True)
    e_date = models.DateField('Event Date',auto_now_add=True)
    desc = models.TextField('Description')
    p_limit = models.IntegerField('Participant Limit')
    brochure = models.ImageField('Event Poster', upload_to=path_and_rename,null=True)
    e_type = models.CharField('Event Type',max_length=188,default='College Fest')
    reg_fee = models.CharField("Registration Fee",default="Free",max_length=100)
    # participants = models.ManyToManyField(Student,on_delete=models.CASCADE)
    Venue = models.CharField(max_length=255)

    def __str__(self):
        return self.e_name

class Club(models.Model):
    c_name = models.CharField('Club Name',max_length=255)
    c_about = models.TextField('About')
    profile_pic = models.ImageField('Profile Pic',upload_to='club')
    events = models.ForeignKey(Event,on_delete=models.CASCADE,blank=True,null=True)
    
    #c_admin = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.c_name
    
class Notification(models.Model):
    title = models.CharField(max_length=160)
    desc = models.TextField('Description',blank=True)
    time = models.TimeField(auto_now=True)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
