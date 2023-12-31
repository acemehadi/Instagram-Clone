from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views 

app_name = "feed"

urlpatterns = [
        path('', views.feed, name='feed'),
]

