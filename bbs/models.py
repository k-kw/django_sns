from django.db import models
from userprofile.models import Userprofile
from django.utils import timezone

# Create your models here.
class Postmsg(models.Model):
    userprf=models.ForeignKey(Userprofile, on_delete=models.DO_NOTHING)
    msg=models.CharField(max_length=5000, blank=False, null=False)
    img=models.ImageField(upload_to='postimgs/', blank=True, null=True)
    imgflg=models.BooleanField(default=True)
    createtime=models.DateTimeField(default=timezone.now)

class Re_postmsg(models.Model):
    userprf=models.ForeignKey(Userprofile, on_delete=models.DO_NOTHING)
    target_msg=models.ForeignKey(Postmsg, on_delete=models.DO_NOTHING)
    msg=models.CharField(max_length=5000, blank=False, null=False)
    img=models.ImageField(upload_to='postimgs/', blank=True, null=True)
    imgflg=models.BooleanField(default=True)
    createtime=models.DateTimeField(default=timezone.now)