from django.db import models

class News_post(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Краткое описание', max_length=255)
    text = models.TextField('Текст новости')
    date = models.DateTimeField('Дата публикации')



    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title