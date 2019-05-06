from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
    email = models.EmailField(verbose_name="email", db_index=True, blank=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Имя", db_index=True, blank=True)
    second_name = models.CharField(verbose_name="Фамилия", max_length=150, db_index=True, blank=True)
    title = models.CharField(verbose_name="Заголовок", max_length=500)
    preview = models.CharField(verbose_name= "Тизер", max_length=500, blank=True, db_index=True)
    text_post = MarkdownxField(verbose_name= "Текст поста", blank=True, db_index=True)
    CHOICE_TO_STAR = (
        (True, 'Пост известной личности'),
        (False, 'Пост обычного пользователя'),
    )
    star = models.BooleanField(verbose_name="Настройка поста", choices=CHOICE_TO_STAR, default=False)
    date_pub = models.DateTimeField(verbose_name="Дата публикации", auto_now_add=True)
    date_modified = models.DateTimeField(verbose_name="Последнее изменение", auto_now=True)
    pictures = models.CharField(verbose_name="Ссылка на картинку", max_length=500, blank=True)

    class Meta:
        ordering = ["-date_modified"]

    def text_post_markdown(self):
        return markdownify(self.text_post)

    def get_preview(self):
        if not self.preview:
            return markdownify(self.text_post[:501]+"...")
        else:
            return self.preview

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return self.title