from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from accounts.models import UserProfile
from post.models import Post
from .forms import CommentForm

@login_required
def feed(request):
    user_profile = UserProfile.objects.get(user=request.user)
    followed_users = user_profile.following.all()
    posts = Post.objects.filter(user__in = followed_users).order_by('-created_at')
    return render(request, 'feed/feed.html', {'posts': posts})


