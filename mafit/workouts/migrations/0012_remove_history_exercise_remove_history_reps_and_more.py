# Generated by Django 4.2.6 on 2023-11-15 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0011_alter_exercise_author_alter_exercise_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='exercise',
        ),
        migrations.RemoveField(
            model_name='history',
            name='reps',
        ),
        migrations.RemoveField(
            model_name='history',
            name='sets',
        ),
        migrations.RemoveField(
            model_name='history',
            name='weight',
        ),
        migrations.AlterField(
            model_name='exercise',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/', verbose_name='Изображение'),
        ),
        migrations.CreateModel(
            name='HistoryExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sets', models.PositiveSmallIntegerField(default=0, help_text='Количество подходов')),
                ('reps', models.PositiveSmallIntegerField(default=0, help_text='Количество повторений')),
                ('weight', models.FloatField(default=0, help_text='Вес')),
                ('exercise', models.ForeignKey(help_text='Упражнение', null=True, on_delete=django.db.models.deletion.SET_NULL, to='workouts.exercise')),
                ('history', models.ForeignKey(help_text='История', null=True, on_delete=django.db.models.deletion.SET_NULL, to='workouts.history')),
            ],
            options={
                'verbose_name': 'История упражнения',
                'verbose_name_plural': 'История упражнений',
                'default_related_name': 'history_exercise',
            },
        ),
    ]