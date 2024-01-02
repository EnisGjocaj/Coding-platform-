from django.contrib import admin

from . models import Post, UserProfile, AgentProfile, SalesData

# Register your models here.

admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(AgentProfile)
admin.site.register(SalesData)

