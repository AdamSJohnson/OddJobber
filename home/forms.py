from django.forms import ModelForm
from django.contrib.auth.models import User
from . models import UserProfile
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', ]