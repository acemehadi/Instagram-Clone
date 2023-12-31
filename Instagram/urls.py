"""
URL configuration for Instagram project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

# App import
from accounts.views import profile, followers, following

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('feed.urls', namespace='feed')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('search/', include('search.urls', namespace='search')),
    path('reels/', include('reels.urls', namespace='reels')),
    path('p/', include('post.urls', namespace='post')),
    path('<str:username>/',
         include(
             [
                 path('', profile, name='profile'),
                 path('followers/', followers, name='followers'),
                 path('following/', following, name='following'),

             ]
         ),
         ),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
