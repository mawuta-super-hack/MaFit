from django.db import models
from django.utils import timezone
from users.models import User

DEFAULT_DATE = timezone.now()

class BaseModelForApp(models.Model):
    """Abstract model for Tag and Muscle."""
    name = models.CharField(max_length=200)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name[:50]


class Muscle(BaseModelForApp):
    """Description of the muscles in the db."""

    class Meta:
        verbose_name = 'Группа мыщц'
        verbose_name_plural = 'Группы мышц'
        default_related_name = 'muscles'


class Tag(BaseModelForApp):
    """Description of the tags in the db."""

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        default_related_name = 'tags'


class Hint(BaseModelForApp):
    """Description of the information about fitness in the db."""
    text = models.TextField()

    class Meta:
        verbose_name = 'Совет'
        verbose_name_plural = 'Советы'
        default_related_name = 'hints'


class Exercise(models.Model):
    """Description of the exercises in the db."""
    name = models.CharField(max_length=200, help_text='Название упражнения')
    image = models.ImageField(
        verbose_name='Изображение',
        blank=True,
        upload_to='media/'
    )
    description = models.TextField(help_text='Описание техники выполнения')
    muscle = models.ManyToManyField(Muscle, related_name='exercise', help_text='Какие мышцы задействованы')
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1, related_name='exercise', help_text='Автор записи')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Упражнения'
        verbose_name_plural = 'Упражнение'
        default_related_name = 'exercises'

    def __str__(self):
        return self.name[:50]


class Workout(models.Model):
    """Description of the workouts in the db."""
    name = models.CharField(verbose_name='Название', max_length=200, help_text='Название тренировки')
    exercises = models.ManyToManyField(Exercise, related_name='exercises', help_text='Упражнения')
    tags = models.ManyToManyField(Tag, related_name='tags', help_text='Теги')
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1, related_name='workout', help_text='Автор записи')
    date = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'
        default_related_name = 'exercises'

    def __str__(self):
        return self.name[:50]


class History(models.Model):
    """Description of the history of trainings in the db."""
    #sets = models.PositiveSmallIntegerField(help_text='Количество подходов')
    #reps = models.PositiveSmallIntegerField(help_text='Количество повторений')
    #weight = models.FloatField(help_text='Вес')
    #exercise = models.ManyToManyField(Exercise, help_text='Упражнение', through='HistoryExercise')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1, help_text='Автор записи', related_name='history')
    workout = models.ForeignKey(Workout, on_delete=models.SET_NULL, null=True, help_text='Связанная тренировка')
    comment = models.TextField(help_text='Комментарий к тренировке', null=True, blank=True)
    date = models.DateField(help_text='Дата тренировки', default=DEFAULT_DATE)

    class Meta:
        verbose_name = 'История тренировки'
        verbose_name_plural = 'История тренировок'
        default_related_name = 'history'

    def __str__(self):
        return f'{self.workout} {self.author}'
    

class HistoryExercise(models.Model):
    """."""
    sets = models.PositiveSmallIntegerField(help_text='Количество подходов', default=0)
    reps = models.PositiveSmallIntegerField(help_text='Количество повторений', default=0)
    weight = models.FloatField(help_text='Вес', default=0)
    exercises = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='HistoryExercise', help_text='Упражнения')
    #date = models.DateField(help_text='Дата тренировки', default=date.today())
    history = models.ForeignKey(History, on_delete=models.CASCADE, related_name='historyexercise')
    #workout = models.ForeignKey(Workout, on_delete=models.SET_NULL, null=True, help_text='Связанная тренировка')
    #history = models.ForeignKey(History, on_delete=models.SET_NULL, null=True, help_text='История',related_name='HistoryExercise')

    class Meta:
        verbose_name = 'История упражнения'
        verbose_name_plural = 'История упражнений'
        default_related_name = 'history_exercise'

    def __str__(self):
        return f'exercise - {self.exercises}:{self.history}'
    

class Favorites(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite',
        verbose_name='Пользователь')
    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Тренировка')

    class Meta:
        verbose_name_plural = "Избранные"
        constraints = (models.UniqueConstraint(fields=['user', 'workout'], name='unique_combination'),)