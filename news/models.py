from django.db import models


class article(models.Model):
    title = models.CharField('Название', max_length=50, default='123')
    announce = models.CharField('Анонс', max_length=255, default='123')
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Время и дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'