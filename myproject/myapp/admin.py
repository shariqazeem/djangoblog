from django.contrib import admin

# Register your models here.
from .models import Course
from .models import RCourse
from .models import Caraousel
from .models import Comment
from .models import ImageModel

admin.site.register(Course)
admin.site.register(RCourse)
admin.site.register(Caraousel)
admin.site.register(Comment)
admin.site.register(ImageModel)