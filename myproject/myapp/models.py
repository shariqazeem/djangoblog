from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    description  = models.TextField()
    image = models.ImageField(upload_to='course_images')
    is_free = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class RCourse(models.Model):
    title = models.CharField(max_length=100)
    description  = models.TextField()
    image = models.ImageField(upload_to='rcourse_images')

    def __str__(self):
        return self.title
    
class Caraousel(models.Model):
    image = models.ImageField(upload_to='carousel_images')

    def __str__(self):
        return str(self.image)

