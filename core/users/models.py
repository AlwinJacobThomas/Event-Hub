import os,uuid
from django.utils.deconstruct import deconstructible
from django.db import models


from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.
#---------------path specifier---------------
@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid.uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join('users/profile/', filename)

path_and_rename = PathAndRename("users/profile/")
#---------------end path specifier---------------

#-----------Account manager----------------------
class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("User must have an email")
        if not username:
            raise ValueError("User must have a username")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,username,password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user    
#-----------end Account manager------------------

#-----------Account User----------------------

class Account(AbstractBaseUser):
    email               = models.EmailField(verbose_name="email",max_length=60,unique=True)
    username            = models.CharField(max_length=30,unique=True)
    date_joined         = models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name="last login",auto_now=True)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)

    #profile_image       = models.ImageField(upload_to=path_and_rename,null=True,blank=True,default="users/profile/default.png")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects =  MyAccountManager()

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
      return True

    def has_module_perms(self, app_label):
      return True


class Club(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)        
    desc = models.TextField('Description')
    profile_pic = models.ImageField(upload_to=path_and_rename,null=True,blank=True,default="users/profile/default.png")
    def __str__(self):
        return str(self.user)
        