from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

from .models import Board


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateBoardForm(ModelForm):
    class Meta:
        model = Board
        
        fields = ['title', 'date_created', 'user', 'date_created', 'archive']
