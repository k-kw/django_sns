from django import forms

class Userfindform(forms.Form):
    findstring=forms.CharField(label="検索したいユーザ名")