# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class UserInheritance(models.Model):
    who_rated = models.ForeignKey(verbose_name='Оценивший пользователь', to=User, related_name='who_rated')
    rated_user = models.ForeignKey(verbose_name='Оцениваемый пользователь', to=User, related_name='rated_user')


class Weight(UserInheritance):
    professionalism = models.IntegerField(verbose_name='Профессионализм',
                                          validators=[MaxValueValidator(10), MinValueValidator(1)])
    control = models.IntegerField(verbose_name='Управление', validators=[MaxValueValidator(10), MinValueValidator(1)])
    communication = models.IntegerField(verbose_name='Коммуникация',
                                        validators=[MaxValueValidator(10), MinValueValidator(1)])
    client_orientation = models.IntegerField(verbose_name='Клиентоориентированность',
                                             validators=[MaxValueValidator(10), MinValueValidator(1)])
    efficiency = models.IntegerField(verbose_name='Эффективность, качество работы',
                                     validators=[MaxValueValidator(10), MinValueValidator(1)])
    evolution = models.IntegerField(verbose_name='Ориентация на развитие',
                                    validators=[MaxValueValidator(10), MinValueValidator(1)])
    leader = models.IntegerField(verbose_name='Лидерство', validators=[MaxValueValidator(10), MinValueValidator(1)])
    teamwork = models.IntegerField(verbose_name='Работа в команде',
                                   validators=[MaxValueValidator(10), MinValueValidator(1)])


class ProfessionalismMark(UserInheritance):
    duty_knowledge = models.IntegerField(verbose_name='Знание функциональных обязанностей',
                                         validators=[MaxValueValidator(10), MinValueValidator(1)])
    motivation = models.IntegerField(verbose_name='Уровень профессиональной мотивации',
                                     validators=[MaxValueValidator(10), MinValueValidator(1)])
    time_management = models.IntegerField(
        verbose_name="Рациональное распределение ресурсов для выполнения обязанностей (время, план работы)",
        validators=[MaxValueValidator(10), MinValueValidator(1)])
    details_knowledge = models.IntegerField(verbose_name='Знание тонкостей и деталей',
                                            validators=[MaxValueValidator(10), MinValueValidator(1)])
    IT_knowledge = models.IntegerField(verbose_name='Знание программных продуктов/ Владение ИТ',
                                       validators=[MaxValueValidator(10), MinValueValidator(1)])

    learnability = models.IntegerField(verbose_name='Обучаемость',
                                       validators=[MaxValueValidator(10), MinValueValidator(1)])

    work_interest = models.IntegerField(verbose_name='Заинтересованность в работе',
                                        validators=[MaxValueValidator(10), MinValueValidator(1)])

    reliability = models.IntegerField(verbose_name='Профессиональная надежность',
                                      validators=[MaxValueValidator(10), MinValueValidator(1)])


class ControlMark(UserInheritance):
    feedback = models.IntegerField(verbose_name='Предоставление обратной связи подчиненным',
                                   validators=[MaxValueValidator(10), MinValueValidator(1)])
    motivation = models.IntegerField(verbose_name='Уровень профессиональной мотивации',
                                     validators=[MaxValueValidator(10), MinValueValidator(1)])
    personal = models.IntegerField(verbose_name='Расстановка персонала',
                                   validators=[MaxValueValidator(10), MinValueValidator(1)])
    affair = models.IntegerField(verbose_name='Состояние дел в возглавляемом коллективе',
                                 validators=[MaxValueValidator(10), MinValueValidator(1)])
    delegation = models.IntegerField(verbose_name='Умение делегировать полномочия',
                                     validators=[MaxValueValidator(10), MinValueValidator(1)])
    goal = models.IntegerField(verbose_name='Умение ставить цели и задачи перед коллективом',
                               validators=[MaxValueValidator(10), MinValueValidator(1)])


class CommunicationMark(UserInheritance):
    conflict_free = models.IntegerField(verbose_name='Бесконфликтность',
                                        validators=[MaxValueValidator(10), MinValueValidator(1)])
    communication = models.IntegerField(verbose_name='Навыки общения',
                                        validators=[MaxValueValidator(10), MinValueValidator(1)])
    diplomacy = models.IntegerField(verbose_name='Дипломатичность',
                                    validators=[MaxValueValidator(10), MinValueValidator(1)])
    thoughts = models.IntegerField(verbose_name='Способность выражать мысли в устной и письменной форме',
                                   validators=[MaxValueValidator(10), MinValueValidator(1)])


class ClientOrientationMark(UserInheritance):
    contact = models.IntegerField(verbose_name='Отношения с клиентом',
                                  validators=[MaxValueValidator(10), MinValueValidator(1)])
    requirements = models.IntegerField(verbose_name='Фокус на потребностях клиента',
                                       validators=[MaxValueValidator(10), MinValueValidator(1)])
    service = models.IntegerField(verbose_name='Уровень обслуживания клиента',
                                  validators=[MaxValueValidator(10), MinValueValidator(1)])
    accompaniment = models.IntegerField(verbose_name='Сопровождение клиента',
                                        validators=[MaxValueValidator(10), MinValueValidator(1)])
    dissemination = models.IntegerField(
        verbose_name='Распространение полезной информации о компании, проектах, продуктах',
        validators=[MaxValueValidator(10), MinValueValidator(1)])


class EfficiencyMark(UserInheritance):
    quality = models.IntegerField(verbose_name='Качество работы',
                                  validators=[MaxValueValidator(10), MinValueValidator(1)])
    planning = models.IntegerField(verbose_name='Планирование (рабочий день)',
                                   validators=[MaxValueValidator(10), MinValueValidator(1)])
    timely = models.IntegerField(
        verbose_name='Своевременное выполнение работы (качественно/профессионально)',
        validators=[MaxValueValidator(10), MinValueValidator(1)])
    performance = models.IntegerField(verbose_name='Производительность труда',
                                      validators=[MaxValueValidator(10), MinValueValidator(1)])
    efficiency = models.IntegerField(verbose_name='Эффективность в достижении целей',
                                     validators=[MaxValueValidator(10), MinValueValidator(1)])


class EvolutionMark(UserInheritance):
    innovations = models.IntegerField(verbose_name='Ориентация на инновации',
                                      validators=[MaxValueValidator(10), MinValueValidator(1)])
    info = models.IntegerField(
        verbose_name='Работа с использованием информации (предложение новых акций, реклама каких-либо услуг)',
        validators=[MaxValueValidator(10), MinValueValidator(1)])
    strategies = models.IntegerField(verbose_name='Работа со стратегиями',
                                     validators=[MaxValueValidator(10), MinValueValidator(1)])
    targeting = models.IntegerField(verbose_name='Целеполагание',
                                    validators=[MaxValueValidator(10), MinValueValidator(1)])
    mistakes = models.IntegerField(verbose_name='Способность учиться на ошибках и не повторять их',
                                   validators=[MaxValueValidator(10), MinValueValidator(1)])


class LeadershipMark(UserInheritance):
    initiative = models.IntegerField(verbose_name='Инициатива',
                                     validators=[MaxValueValidator(10), MinValueValidator(1)])
    independence = models.IntegerField(verbose_name='Самостоятельность',
                                       validators=[MaxValueValidator(10), MinValueValidator(1)])
    relations = models.IntegerField(verbose_name='Ориентированность на результат',
                                    validators=[MaxValueValidator(10), MinValueValidator(1)])
    relations_focus = models.IntegerField(
        verbose_name='Ориентированность на отношения (быть заинтересованным в более профессиональном общении, поведении с коллегами, руководителями, с каждым клиентом)',
        validators=[MaxValueValidator(10), MinValueValidator(1)])
    formal_leadership = models.IntegerField(verbose_name='Формальное лидерство (профессиональное)',
                                            validators=[MaxValueValidator(10), MinValueValidator(1)])
    informal_leadership = models.IntegerField(verbose_name='Неформальное лидерство (в социуме)',
                                              validators=[MaxValueValidator(10), MinValueValidator(1)])


class TeamworkMark(UserInheritance):
    loyalty = models.IntegerField(verbose_name='Преданность компании',
                                  validators=[MaxValueValidator(10), MinValueValidator(1)])
    teamwork = models.IntegerField(verbose_name='Умение работать в команде',
                                   validators=[MaxValueValidator(10), MinValueValidator(1)])
    entry_speed = models.IntegerField(verbose_name='Скорость вхождения в коллектив',
                                      validators=[MaxValueValidator(10), MinValueValidator(1)])
    adoption_speed = models.IntegerField(verbose_name='Скорость принятия нового члена коллектива',
                                         validators=[MaxValueValidator(10), MinValueValidator(1)])
    general_rhythm = models.IntegerField(verbose_name='Умение работать в общем ритме',
                                         validators=[MaxValueValidator(10), MinValueValidator(1)])
    emotions_control = models.IntegerField(
        verbose_name='Умение управлять эмоциями, не проявлять личных симпатий и антипатий',
        validators=[MaxValueValidator(10), MinValueValidator(1)])
    listen = models.IntegerField(verbose_name='Умение принимать чужую точку зрения и признавать свои ошибки',
                                 validators=[MaxValueValidator(10), MinValueValidator(1)])
    delegate = models.IntegerField(verbose_name='Умение делегировать полномочия',
                                   validators=[MaxValueValidator(10), MinValueValidator(1)])
    objectives_lead = models.IntegerField(verbose_name='Умение руководить  в зависимости от целей',
                                          validators=[MaxValueValidator(10), MinValueValidator(1)])
    objectives_comply = models.IntegerField(verbose_name='Умение подчиняться в зависимости от целей',
                                            validators=[MaxValueValidator(10), MinValueValidator(1)])
    help = models.IntegerField(verbose_name='Умение смирять личные амбиции и оказывать помощь коллегам',
                               validators=[MaxValueValidator(10), MinValueValidator(1)])
