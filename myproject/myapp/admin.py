from django.contrib import admin

# Register your models here.
from .models import Video
from .models import RCourse
from .models import Caraousel
from .models import Comment
from .models import ImageModel

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order',)  # Specify the fields you want to display
    list_editable = ('order',)


admin.site.register(Video, VideoAdmin)
admin.site.register(RCourse)
admin.site.register(Caraousel)
admin.site.register(Comment)
admin.site.register(ImageModel)