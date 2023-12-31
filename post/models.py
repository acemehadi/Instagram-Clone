from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts',blank=True, null=True)
    caption = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid4,unique=True)

    def __str__(self):
        return f"Post by {self.user.username} on {self.created_at}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text
