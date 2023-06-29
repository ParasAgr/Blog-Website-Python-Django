from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
