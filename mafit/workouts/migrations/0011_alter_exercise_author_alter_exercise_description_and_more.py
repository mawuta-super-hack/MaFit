# Generated by Django 4.2.6 on 2023-10-29 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workouts', '0010_remove_userweight_user_delete_user_delete_userweight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='author',
            field=models.ForeignKey(default=1, help_text='Автор записи', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='exercise', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='description',
            field=models.TextField(help_text='Описание техники выполнения'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='image',
            field=models.ImageField(blank=True, upload_to='exercise/', verbose_name='Изображение'),
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='muscle',
        ),
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(help_text='Название упражнения', max_length=200),
        ),
        migrations.AlterField(
            model_name='history',
            name='author',
            field=models.ForeignKey(default=1, help_text='Автор записи', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateField(help_text='Дата тренировки'),
        ),
        migrations.AlterField(
            model_name='history',
            name='exercise',
            field=models.ManyToManyField(help_text='Упражнение', to='workouts.exercise'),
        ),
        migrations.AlterField(
            model_name='history',
            name='reps',
            field=models.PositiveSmallIntegerField(help_text='Количество повторений'),
        ),
        migrations.AlterField(
            model_name='history',
            name='sets',
            field=models.PositiveSmallIntegerField(help_text='Количество подходов'),
        ),
        migrations.AlterField(
            model_name='history',
            name='weight',
            field=models.FloatField(help_text='Вес'),
        ),
        migrations.AlterField(
            model_name='history',
            name='workout',
            field=models.ForeignKey(help_text='Связанная тренировка', null=True, on_delete=django.db.models.deletion.SET_NULL, to='workouts.workout'),
        ),
        migrations.AlterField(
            model_name='workout',
            name='author',
            field=models.ForeignKey(default=1, help_text='Автор записи', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='workout', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercises',
            field=models.ManyToManyField(help_text='Упражнения', related_name='exercises', to='workouts.exercise'),
        ),
        migrations.AlterField(
            model_name='workout',
            name='name',
            field=models.CharField(help_text='Название тренировки', max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='workout',
            name='tags',
            field=models.ManyToManyField(help_text='Теги', related_name='tags', to='workouts.tag'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='muscle',
            field=models.ManyToManyField(help_text='Какие мышцы задействованы', related_name='exercise', to='workouts.muscle'),
        ),
    ]