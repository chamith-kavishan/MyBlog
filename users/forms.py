from django import forms
from django.contrib.auth.models import User as AuthUser
from .models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = AuthUser
        fields = ['username', 'email', 'password']

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'post_image', 'bio']
