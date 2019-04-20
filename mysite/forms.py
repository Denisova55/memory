from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'second_name', 'email','title', 'preview', 'text_post', 'pictures', )


