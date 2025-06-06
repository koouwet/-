# Generated by Django 4.2.20 on 2025-04-23 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('path', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='path',
            name='access',
            field=models.CharField(max_length=30, verbose_name='Подтверждение доступности'),
        ),
        migrations.AlterField(
            model_name='path',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='path',
            name='text',
            field=models.CharField(max_length=250, verbose_name='Описание'),
        ),
    ]
