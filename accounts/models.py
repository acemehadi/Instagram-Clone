from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=2)
    profile_photo = models.ImageField(
        upload_to='profile', default='profile/default.jpg')
    bio = models.TextField(max_length=100, blank=True)
    following = models.ManyToManyField(User, blank=True, related_name='followers')
    followers = models.ManyToManyField(User, blank=True, related_name='following')


    def __str__(self):
        return self.user.username

