from django.contrib import admin

from . models import Category, VideoModel, LabTypeModel
# Register your models here.

admin.site.register(Category)
admin.site.register(VideoModel)
admin.site.register(LabTypeModel)

