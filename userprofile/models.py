from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userprofile(models.Model):
    user=models.OneToOneField(User, on_delete=models.DO_NOTHING)
    msg=models.CharField(max_length=1000)
    prfimg=models.ImageField(upload_to='prfimgs/')