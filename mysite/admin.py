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
    list_display = ('word', )


class AdminLinkWordInline(admin.StackedInline):
    model = LinkWord.base_words.through
    extra = 0


@admin.register(BasicWord)
class AdminBasicWord(admin.ModelAdmin):
    list_display = ('word', )
    inlines = [
        AdminLinkWordInline
    ]
