from django import forms

from .models import UserProfile

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class  RegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, label='Full Name')

    class Meta:
        model = User
        fields = ['email', 'username','full_name']



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_photo', 'bio','full_name']
