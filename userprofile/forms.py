from django import forms
from .models import Userprofile
#user profile form
class UserprofileForm(forms.ModelForm):
    class Meta:
        model=Userprofile
        fields=['msg', 'prfimg']