from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField('Почта', max_length=100, unique=True, help_text='Эл.почта')
    username = models.CharField(
        'Никнэйм', max_length=50, unique=True, help_text='Никнейм')
    #last_weight = models.FloatField(null=True, default=0.0)
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
    

class UserWeight(models.Model):
    """Description of the weight in the db."""
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1, related_name='weight', help_text='Пользователь')
    date = models.DateField(help_text='Дата')
    weight = models.FloatField(help_text='Вес в указазанную дату')

    class Meta:
        verbose_name = 'Вес пользователя'
        verbose_name_plural = 'Вес пользователей'
        default_related_name = 'weight'
