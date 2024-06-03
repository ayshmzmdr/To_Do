from django import forms
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class signupForm(UserCreationForm):
    email=forms.EmailField()
    age=forms.IntegerField()

    class Meta():
        model=User
        fields=["username","email","age","password1","password2"]

