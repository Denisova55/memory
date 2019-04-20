from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview', 'text_post', 'star', 'name', 'second_name')

admin.site.register(Post, PostAdmin)

