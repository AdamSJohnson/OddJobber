from django.forms import ModelForm
from django.contrib.auth.models import User
from . models import UserProfile

class UserForm(ModelForm):
    class Meta:
        model = User

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']