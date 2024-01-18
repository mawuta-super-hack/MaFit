# Generated by Django 4.2.6 on 2023-12-26 21:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0017_workout_comment_alter_history_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='comment',
        ),
        migrations.AddField(
            model_name='history',
            name='comment',
            field=models.TextField(blank=True, help_text='Комментарий к тренировке', null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 12, 26, 21, 10, 36, 884389, tzinfo=datetime.timezone.utc), help_text='Дата тренировки'),
        ),
    ]