from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Post,Like
from .forms import PostForm,CommentForm

# Create your views here.

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('feed:feed')
    else:
        form = PostForm()

    return render(request, 'post/create_post.html', {'form':form})

def post_detail(request, uuid):
    post = get_object_or_404(Post,uuid=uuid)
    like_count = Like.objects.filter(post=post).count()
    return render(request, 'post/post_detail.html', {'post':post, 'like_count' : like_count})

def add_comment(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            return redirect("feed:feed")


def like_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = request.user

    # Check if the user has already liked the post
    if Like.objects.filter(user=user, post=post).exists():
        # User has already liked the post, so unlike it
        Like.objects.filter(user=user, post=post).delete()
    else:
        # User hasn't liked the post, so like it
        Like.objects.create(user=user, post=post)

    return HttpResponse("DOne")

