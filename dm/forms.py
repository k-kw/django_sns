from django import forms
from .models import Dm
# BBS message form
class DmForm(forms.ModelForm):
    class Meta:
        model = Dm
        fields=['msg','img']