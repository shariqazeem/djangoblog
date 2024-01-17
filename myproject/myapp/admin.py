from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

# Register your models here.
from .models import Video
from .models import RCourse
from .models import Caraousel
from .models import Comment
from .models import ImageModel
from .models import Applicant
from .models import Blog

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order',)  # Specify the fields you want to display
    list_editable = ('order',)

admin.site.register(Blog)
admin.site.register(Applicant)
admin.site.register(Video, VideoAdmin)
admin.site.register(RCourse)
admin.site.register(Caraousel)
admin.site.register(Comment)
admin.site.register(ImageModel)