from django.db import models
from userprofile.models import Userprofile
from django.utils import timezone

# Create your models here.
class Follow(models.Model):
    flwee_prf=models.ForeignKey(Userprofile, on_delete=models.DO_NOTHING, related_name='followee')
    flwer_prf=models.ForeignKey(Userprofile, on_delete=models.DO_NOTHING, related_name='follower')
    ctime=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return 'created: '+str(self.ctime)+', followee_id: '+str(self.flwee_prf)+', follower_id: '+str(self.flwer_prf)