from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class RCourse(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    recommended = models.BooleanField(default=False)  # Add this field
    image = models.ImageField(upload_to='rcourse_images')
    video_link = models.CharField(max_length=200, default='')  # Add this field for video links
    overview = models.TextField(blank=True)
    q_and_a = models.TextField(blank=True)
    announcements = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
class Video(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    overview = models.TextField(blank=True)
    q_and_a = models.TextField(blank=True)
    announcements = models.TextField(blank=True)
    course = models.ForeignKey(RCourse, on_delete=models.CASCADE, related_name='videos')
    order = models.PositiveIntegerField(default=0)

    
class Caraousel(models.Model):
    image = models.ImageField(upload_to='carousel_images')

    def __str__(self):
        return str(self.image)
    
class ImageModel(models.Model):
    image = models.ImageField(upload_to='images')  # Define the path where the images will be stored

    def __str__(self):
        return str(self.image)
    
class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments', null=True, default=None)
    course = models.ForeignKey(RCourse, on_delete=models.CASCADE, related_name='comments', null=True, default=None)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, default="Anonymous")

class Applicant(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    resume_link = models.URLField()
    skills = models.CharField(max_length=50)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



