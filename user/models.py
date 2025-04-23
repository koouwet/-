from django.db import models

class data(models.Model):
    name = models.CharField('Имя', max_length=15)
    surname = models.CharField('Фамилия', max_length=15)
    contact = models.CharField('Контактные данные', max_length=30)
    ovz = models.CharField('Тип ОВЗ', max_length=15)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
