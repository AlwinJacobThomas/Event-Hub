from django.contrib import admin
from .models import Account,Club,Student
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email','username',)
    search_fields = ('username',)
    readonly_fields = ('id','date_joined','last_login',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)  
admin.site.register(Club)
admin.site.register(Student)
