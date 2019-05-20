import re

from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'preview', 'text_post', 'pictures', )

    def clean_text_post(self):
        value = self.cleaned_data.get('text_post')
        if value is not None:
            words = StopWords.objects.values_list('stop_word', flat=True)
            escape_words = (re.escape(w) for w in words)
            pattern = ('|'.join(escape_words))
            value = re.sub(pattern, ' ', value)
        return value


class UserCreationForm(UserCreationForm):
    city = forms.CharField(label="City", max_length=50, required=True)
    country = forms.CharField(label="Country", max_length=100, required=True)
    first_name = forms.CharField(label="First name", max_length=50, required=True)
    second_name = forms.CharField(label="Second name", max_length=50, required=True)
    age = forms.CharField(label="Age", max_length=3, required=True)
    contacts = forms.CharField(label="Contacs", max_length=200, required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "city", "first_name", "second_name", "age", "country",
                  "contacts")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.city = self.cleaned_data["city"]
        user.country = self.cleaned_data["country"]
        user.first_name = self.cleaned_data["first_name"]
        user.second_name = self.cleaned_data["second_name"]
        user.age = self.cleaned_data["age"]
        user.contacts = self.cleaned_data["contacts"]

        if commit:
            user.save()
        return user

