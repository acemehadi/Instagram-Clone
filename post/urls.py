from django.urls import path

app_name = 'post'

from . import views

urlpatterns = [
        path('create-post/', views.create_post, name="create_post"),
        path('<str:uuid>/', views.post_detail, name="post_detail"),
        path('<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
        path('<int:post_id>/like_post/', views.like_post, name='like_post'),
]

