# -*- coding: utf-8 -*-
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

DEPARTMENT_CHOICES = (
    ('1', 'Тестовый департамент'),
)


class User(AbstractUser):
    first_name = models.CharField(verbose_name=u'Имя', blank=False, max_length=30)
    patronymic_name = models.CharField(verbose_name=u'Отчество', blank=False, max_length=30)
    last_name = models.CharField(verbose_name=u'Фамилия', blank=False, max_length=30)
    department = models.CharField(choices=DEPARTMENT_CHOICES, max_length=30)
    token = models.CharField(max_length=32, blank=True, null=True, db_index=True, unique=True)

    def save(self, *args, **kwargs):
        if self.token == '' or self.token is None:
            self.token = str(uuid.uuid4().hex)
        super(User, self).save(*args, **kwargs)
