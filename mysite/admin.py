from django.contrib import admin
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview', 'text_post', 'star', 'name', 'second_name')


@admin.register(StopWords)
class StopWords(admin.ModelAdmin):
    list_display = ('stop_word', )


@admin.register(LinkWord)
class AdminLinkWord(admin.ModelAdmin):
    list_display = ('link_word', )


@admin.register(BasicWord)
class AdminBasicWord(admin.ModelAdmin):
    list_display = ('basic_word', )
