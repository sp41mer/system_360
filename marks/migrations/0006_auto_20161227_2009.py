# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0005_auto_20161226_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientorientationmark',
            name='sum_of_all',
            field=models.IntegerField(default=0, verbose_name='Сумма характеристик'),
        ),
        migrations.AddField(
            model_name='communicationmark',
            name='sum_of_all',
            field=models.IntegerField(default=0, verbose_name='Сумма характеристик'),
        ),
        migrations.AddField(
            model_name='controlmark',
            name='sum_of_all',
            field=models.IntegerField(default=0, verbose_name='Сумма характеристик'),
        ),
        migrations.AddField(
            model_name='efficiencymark',
            name='sum_of_all',
            field=models.IntegerField(default=0, verbose_name='Сумма характеристик'),
        ),
        migrations.AddField(
            model_name='evolutionmark',
            name='sum_of_all',
            field=models.IntegerField(default=0, verbose_name='Сумма характеристик'),
        ),
        migrations.AddField(
            model_name='leadershipmark',
            name='sum_of_all',
            field=models.IntegerField(default=0, verbose_name='Сумма характеристик'),
        ),
        migrations.AddField(
            model_name='professionalismmark',
            name='sum_of_all',
            field=models.IntegerField(default=0, verbose_name='Сумма характеристик'),
        ),
        migrations.AddField(
            model_name='teamworkmark',
            name='sum_of_all',
            field=models.IntegerField(default=0, verbose_name='Сумма характеристик'),
        ),
    ]
