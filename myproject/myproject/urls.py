"""
URL configuration for myproject project.

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
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('courses/', views.CoursesPage, name='courses'),
    path('playlist-videos/<str:playlist_id>/', views.playlist_videos, name='playlist_videos'),
    path('video-player/<str:video_id>/', views.video_player, name='video_player'), 
    path('watch/<str:course_title>/', views.watch_course, name='watch_course'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('contact/', views.ContactPage, name='contact'),
    path('video/<int:video_id>/', views.video_detail, name='video_detail'),
    path('video_detail/<int:video_id>/', views.video_detail, name='video_detail'),
    path('workwithus/', views.WorkWithUsPage, name='workwithus'),
    path('apply/', views.apply_now, name='apply_now'),
    path('blog/', views.BlogPage, name='blog'),
    path('blog/<str:blog_title>/', views.BlogDetail, name='blog_detail'),



    path('sitemap.xml', TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml")),







] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


