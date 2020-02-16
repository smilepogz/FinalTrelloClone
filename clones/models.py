from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

#Add Board on Home page board
class Board(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    archive = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class BoardList(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class BoardMember(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activation = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    # boardList = models.ForeignKey(BoardList, on_delete=models.CASCADE)

# Card Details
class Card(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=10, blank=True)    
    date_created = models.DateField(default=timezone.now)
    archive = models.BooleanField(default=False)
    Attachment = models.FileField()

    def __str__(self):
        return self.title

    
class BoardInvite(models.Model):
    email = models.EmailField(max_length=50, blank=True)
    token = models.UUIDField(default=uuid.uuid4)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    activation = models.BooleanField(default=False)
    invite_to = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    archive = models.BooleanField(default=False)
 


class Activity(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=100)

    
    def __str__(self):
        return self.created_by


class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=timezone.now)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
