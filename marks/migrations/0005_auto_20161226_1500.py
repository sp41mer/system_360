# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 15:00
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0004_auto_20161226_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='efficiencymark',
            name='timely',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Своевременное выполнение работы (качественно/профессионально)'),
        ),
    ]
