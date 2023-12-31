from django.contrib.auth import authenticate,login
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from .models import UserProfile
from .forms import RegistrationForm, UserProfileForm

from post.models import *

# Create your views here.
def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            full_name = form.cleaned_data.get('full_name')
            UserProfile.objects.create(user=user,full_name=full_name)
            login(request, user)
            return redirect('accounts:login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)

    #user = request.user
    user_profile = UserProfile.objects.get(user=user)
    user_posts = Post.objects.filter(user=user).order_by('-created_at')
    context = {'user_profile': user_profile,
               'user': user,
               'followers' :  user_profile.followers.count(),
               'following' :  user_profile.following.count(),
               'user_posts' : user_posts,
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def edit(request):
    if request.method=="POST":
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile',username=request.user.username)
    else:
        form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'accounts/edit-profile.html', {'form' : form})


@login_required
def follow_user(request, username):
    user_to_follow = User.objects.get(username=username)
    user_profile = UserProfile.objects.get(user=request.user)
    user_to_follow_profile = UserProfile.objects.get(user=user_to_follow)
    
    if user_to_follow != request.user:
        user_profile.following.add(user_to_follow)
        user_to_follow_profile.followers.add(request.user)

    return redirect('profile', username=username)

@login_required
def unfollow_user(request, username):
    user_to_unfollow = User.objects.get(username=username)
    user_to_unfollow_profile = UserProfile.objects.get(user=user_to_unfollow)
    user_profile = UserProfile.objects.get(user=request.user)

    user_profile.following.remove(user_to_unfollow)
    user_to_unfollow_profile.followers.remove(request.user)

    return redirect('profile', username=username)

def followers(request, username):
    user = User.objects.get(username=username)
    userprofile = UserProfile.objects.get(user=user)
    followers = userprofile.followers.all()
    context = {
            'followers': followers,
            'user' : user
    }

    return render(request, 'accounts/followers.html', context)

def following(request, username):
    user = User.objects.get(username=username)
    userprofile = UserProfile.objects.get(user=user)
    following = userprofile.following.all()
    context = {
            'following' : following,
            'user' : user
    }

    return render(request, 'accounts/following.html', context)


