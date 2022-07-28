from django.contrib import admin
from .models import Event,Club,Notification
# Register your models here.
admin.site.register(Event)
admin.site.register(Club)
admin.site.register(Notification)