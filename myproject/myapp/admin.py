from django.contrib import admin

# Register your models here.
from .models import Course
from .models import RCourse
from .models import Caraousel

admin.site.register(Course)
admin.site.register(RCourse)
admin.site.register(Caraousel)