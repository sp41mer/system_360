# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from core.models import User


class Evaluating(models.Model):
    eval_user = models.ForeignKey(related_name='evaluating_user', verbose_name='Оценивающий пользователь', to=User)
    estimated_users = models.ManyToManyField(related_name='estimated_users', verbose_name='Оцениваемые пользователи', to=User)
    already_estimated_users = models.ManyToManyField(related_name='already_estimated', verbose_name='Оцененые пользователи', to=User)

    def __str__(self):
        return u'{} {}'.format(self.eval_user.first_name, self.eval_user.last_name)

    class Meta:
        verbose_name = u'Оценивающий'
        verbose_name_plural = u'Оценивающие'


def add_week():
    return timezone.now() + timezone.timedelta(days=7)


class Interview(models.Model):
    start_date = models.DateField(verbose_name=u'Дата начала опроса', default=timezone.now)
    end_date = models.DateField(verbose_name=u'Дата конца опроса',
                                default=add_week)
    users_to_eval = models.ManyToManyField(Evaluating)

    def __str__(self):
        return u'Начало опроса: {} Конец опроса: {}'.format(self.start_date, self.start_date)

    class Meta:
        verbose_name = u'Опрос'
        verbose_name_plural = u'Опросы'
