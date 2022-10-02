from django import forms
from .models import Postmsg,Re_postmsg
# BBS message form
class PostmsgForm(forms.ModelForm):
    class Meta:
        model = Postmsg
        fields=['msg','img']

class Postmsgfindform(forms.Form):
    findstring=forms.CharField(label="メッセージ検索")


class Re_postmsgForm(forms.ModelForm):
    class Meta:
        model = Re_postmsg
        fields=['msg', 'img']