# Generated by Django 4.2.6 on 2023-10-26 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userweight',
            name='weight',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
