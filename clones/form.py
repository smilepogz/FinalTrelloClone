from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

from .models import Board,Card, BoardList
from django.db import models


class CreateUserForm(UserCreationForm):
    """" Login """
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateBoardForm(ModelForm):
    class Meta:
        model = Board
        
        fields = ['title', 'date_created', 'user', 'date_created', 'archive']


class CreateCardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'description','date_created','archive']


class CreateBoardList(ModelForm):
    class Meta:
        model = BoardList
        fields = ['title','board','date_created']


