from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField('Почта', max_length=100, unique=True)
    username = models.CharField(
        'Никнэйм', max_length=50, unique=True)
    weight_now = models.FloatField(
        help_text='Текущий вес', blank=True, null=True
    )
    weight_purpose = models.FloatField(
        help_text='Желаемый вес', blank=True, null=True
    )
    photo = models.ImageField(
        verbose_name='Изображение',
        blank=True, null=True,
        upload_to='media/'
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
