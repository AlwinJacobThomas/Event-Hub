from django.contrib import admin
from .models import Event,Notification
# Register your models here.
#admin.site.register(Event)

admin.site.register(Notification)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
       list_display = ('e_name',)
       search_fields = ('e_name','e_date')
       ordering = ('e_name',)
