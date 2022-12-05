from django.db import models


class Video(models.Model):
    video_id = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    description = models.TextField(null=True)
    preview = models.CharField(max_length=255, null=True)
    video = models.FileField(upload_to="media/", null=True)
    upload_datetime = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)


class Comment(models.Model):
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
