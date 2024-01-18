from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField('Почта', max_length=100, unique=True)
    username = models.CharField(
        'Никнэйм', max_length=50, unique=True)
    #last_weight = models.FloatField(null=True, default=0.0)
    weight_now = models.FloatField(help_text='Текущий вес', blank=True, null=True )
    weight_purpose = models.FloatField(help_text='Желаемый вес', blank=True, null=True )
    photo = models.ImageField(
        verbose_name='Изображение',
        #default='static/img/profile.jpg',
        blank=True, null= True,
        upload_to='media/'
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
    


    # user = models.OneToOneField(User, on_delete=models.SET_DEFAULT, default=1, related_name='weight', help_text='Вес')
    # #date = models.DateField(help_text='Дата')
    # weight_now = models.FloatField(help_text='Текущий вес', blank=True, null=True, default=0.0)
    # purpose = models.FloatField(help_text='Желаемый вес', blank=True, null=True, default=0.0)
    # photo = models.ImageField(
    #     verbose_name='Изображение',
    #     #default='static/img/profile.jpg',
    #     blank=True, null= True,
    #     upload_to='media/'
    # )

    # class Meta:
    #     verbose_name = 'Вес пользователя'
    #     verbose_name_plural = 'Вес пользователей'
    #     default_related_name = 'weight'


