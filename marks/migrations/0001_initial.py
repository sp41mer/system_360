# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 03:01
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInheritance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ClientOrientationMark',
            fields=[
                ('userinheritance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='marks.UserInheritance')),
                ('contact', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Отношения с клиентом')),
                ('requirements', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Фокус на потребностях клиента')),
                ('service', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Уровень обслуживания клиента')),
                ('accompaniment', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Сопровождение клиента')),
                ('dissemination', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Распространение полезной информации о компании, проектах, продуктах')),
            ],
            bases=('marks.userinheritance',),
        ),
        migrations.CreateModel(
            name='CommunicationMark',
            fields=[
                ('userinheritance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='marks.UserInheritance')),
                ('conflict_free', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Бесконфликтность')),
                ('communication', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Навыки общения')),
                ('diplomacy', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Дипломатичность')),
                ('thoughts', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Способность выражать мысли в устной и письменной форме')),
            ],
            bases=('marks.userinheritance',),
        ),
        migrations.CreateModel(
            name='ControlMark',
            fields=[
                ('userinheritance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='marks.UserInheritance')),
                ('feedback', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Предоставление обратной связи подчиненным')),
                ('motivation', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Уровень профессиональной мотивации')),
                ('personal', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Расстановка персонала')),
                ('affair', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Состояние дел в возглавляемом коллективе')),
                ('delegation', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Умение делегировать полномочия')),
                ('goal', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Умение ставить цели и задачи перед коллективом')),
            ],
            bases=('marks.userinheritance',),
        ),
        migrations.CreateModel(
            name='EfficiencyMark',
            fields=[
                ('userinheritance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='marks.UserInheritance')),
                ('quality', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Качество работы')),
                ('planning', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Планирование (рабочий день)')),
                ('timely', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Своевременное выполнение работы (точно в срок и качественно/профессионально)')),
                ('performance', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Производительность труда')),
                ('efficiency', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Эффективность в достижении целей')),
            ],
            bases=('marks.userinheritance',),
        ),
        migrations.CreateModel(
            name='EvolutionMark',
            fields=[
                ('userinheritance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='marks.UserInheritance')),
                ('innovations', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Ориентация на инновации')),
                ('info', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Работа с использованием информации (предложение новых акций, реклама каких-либо услуг)')),
                ('strategies', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Работа со стратегиями')),
                ('targeting', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Целеполагание')),
                ('mistakes', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Способность учиться на ошибках и не повторять их')),
            ],
            bases=('marks.userinheritance',),
        ),
        migrations.CreateModel(
            name='ProfessionalismMark',
            fields=[
                ('userinheritance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='marks.UserInheritance')),
                ('duty_knowledge', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Знание функциональных обязанностей')),
                ('motivation', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Уровень профессиональной мотивации')),
                ('time_management', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Рациональное распределение ресурсов для выполнения обязанностей (время, план работы)')),
                ('details_knowledge', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Знание тонкостей и деталей')),
                ('IT_knowledge', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Знание программных продуктов/ Владение ИТ')),
                ('learnability', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Обучаемость')),
                ('work_interst', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Заинтересованность в работе')),
                ('reliability', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Профессиональная надежность')),
            ],
            bases=('marks.userinheritance',),
        ),
        migrations.CreateModel(
            name='LeadershipMark',
            fields=[
                ('userinheritance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='marks.UserInheritance')),
                ('initiative', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Инициатива')),
                ('independence', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Самостоятельность')),
                ('relations', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Ориентированность на результат')),
                ('relations_focus', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Ориентированность на отношения (быть заинтересованным в более профессиональном общении, поведении с коллегами, руководителями, с каждым клиентом)')),
                ('formal_leadership', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Формальное лидерство (профессиональное)')),
                ('informal_leadership', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Неформальное лидерство (в социуме)')),
            ],
            bases=('marks.userinheritance',),
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('userinheritance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='marks.UserInheritance')),
                ('professionalism', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Профессионализм')),
                ('control', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Управление')),
                ('communication', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Коммуникация')),
                ('client_orientation', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Клиентоориентированность')),
                ('efficiency', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Эффективность, качество работы')),
                ('evolution', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Ориентация на развитие')),
                ('leader', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Лидерство')),
                ('teamwork', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Работа в команде')),
            ],
            bases=('marks.userinheritance',),
        ),
        migrations.AddField(
            model_name='userinheritance',
            name='rated_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rated_user', to=settings.AUTH_USER_MODEL, verbose_name='Оценивший пользователь'),
        ),
        migrations.AddField(
            model_name='userinheritance',
            name='who_rated',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_rated', to=settings.AUTH_USER_MODEL, verbose_name='Оценивший пользователь'),
        ),
    ]
