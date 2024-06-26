# Generated by Django 4.2.6 on 2023-11-30 20:31

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workouts', '0015_remove_history_exercises_history_workout_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='author',
            field=models.ForeignKey(default=1, help_text='Автор записи', on_delete=django.db.models.deletion.CASCADE, related_name='history', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 11, 30, 20, 31, 2, 343290, tzinfo=datetime.timezone.utc), help_text='Дата тренировки'),
        ),
        migrations.AlterField(
            model_name='historyexercise',
            name='exercises',
            field=models.ForeignKey(default=15, help_text='Упражнения', on_delete=django.db.models.deletion.CASCADE, related_name='HistoryExercise', to='workouts.exercise'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historyexercise',
            name='history',
            field=models.ForeignKey(default=15, on_delete=django.db.models.deletion.CASCADE, related_name='historyexercise', to='workouts.history'),
        ),
    ]
