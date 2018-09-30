from django import forms
from django.contrib.auth.models import User


class Formname(forms.Form):
    user = forms.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput())
    text=forms.CharField(widget=forms.Textarea)
