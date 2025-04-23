from django.db import models

class rewiews(models.Model):
    name = models.CharField('Имя', max_length=50)
    text = models.CharField('Отзыв', max_length=250)
    accessK = models.CharField('Доступность для колясочников', max_length=15)
    accessV = models.CharField('Доступность для слабовидящих', max_length=15)
    accessL = models.CharField('Доступность для слабослышащих', max_length=15)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'