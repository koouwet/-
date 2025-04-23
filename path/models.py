from django.db import models

class path(models.Model):
    name = models.CharField('Название', max_length=50)
    text = models.CharField('Описание', max_length=250)
    access = models.CharField('Подтверждение доступности', max_length=30)
    state = models.CharField('Остановки', max_length=15)
    accessK = models.CharField('Доступность для колясочников', max_length=15)
    accessV = models.CharField('Доступность для слабовидящих', max_length=15)
    accessL = models.CharField('Доступность для слабослышащих', max_length=15)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
