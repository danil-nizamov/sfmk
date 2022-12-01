from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    preview = models.ImageField(upload_to="media/")
    video = models.FileField(upload_to="media/")
    upload_datetime = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    channel = models.OneToOneField(User, on_delete=models.PROTECT)


class Comment(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
