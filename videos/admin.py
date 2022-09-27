from django.contrib import admin
from videos.models import Video, Category, Comment

# Register your models here.

admin.site.register(Video)
admin.site.register(Category)
admin.site.register(Comment)