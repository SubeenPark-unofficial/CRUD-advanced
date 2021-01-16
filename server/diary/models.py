from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(verbose_name='일기의 제목', max_length=100)
    content = models.TextField(verbose_name='일기의 내용')

    created_at = models.DateTimeField(
        verbose_name='일기를 쓴 시간', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='일기를 수정한 시간', auto_now=True)

    def __str__(self):
        return f'{self.id}. {self.title}'
