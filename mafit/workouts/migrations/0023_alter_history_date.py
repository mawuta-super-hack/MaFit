# Generated by Django 4.2.6 on 2024-01-18 17:27

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0022_alter_history_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 1, 18, 17, 27, 3, 922792, tzinfo=datetime.timezone.utc), help_text='Дата тренировки'),
        ),
    ]
