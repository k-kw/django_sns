from django.db import models
from userprofile.models import Userprofile
from django.utils import timezone

# Create your models here.
class Dm(models.Model):
    sdprf=models.ForeignKey(Userprofile, on_delete=models.DO_NOTHING, related_name='sendDm')
    rcvprf=models.ForeignKey(Userprofile, on_delete=models.DO_NOTHING, related_name='rcvDm')
    msg=models.CharField(max_length=5000, blank=False, null=False)
    img=models.ImageField(upload_to='dmimgs/', blank=True, null=True)
    imgflg=models.BooleanField(default=True)
    sdtime=models.DateTimeField(default=timezone.now)
