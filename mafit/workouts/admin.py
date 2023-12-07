from django.contrib import admin
from .models import Muscle, Tag, Hint, Workout, Exercise, History, HistoryExercise


class BaseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


class WorkoutTagline(admin.TabularInline):
    model = Workout.tags.through
    min_num = 1
    extra = 0


class WorkoutExerciseline(admin.TabularInline):
    model = Workout.exercises.through
    min_num = 1
    extra = 0


class ExerciseMuscleline(admin.TabularInline):
    model = Exercise.muscle.through
    min_num = 1
    extra = 0


class ExerciseAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    search_fields = ('name', 'muscle')
    list_filter = ('name', 'muscle')
    empty_value_display = '-не указано-'
    inlines = [ExerciseMuscleline]
    exclude = ['muscle']


class WorkoutAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    search_fields = ('name', 'tags')
    list_filter = ('name', 'tags')
    empty_value_display = '-не указано-'
    inlines = [WorkoutExerciseline, WorkoutTagline]
    exclude = ['tags', 'exercises']

# class Historyline(admin.TabularInline):
#     model = HistoryExercise.history.through
#     min_num = 1
#     extra = 0

class HistoryExerciseAdmin(admin.ModelAdmin):

    fields = ['exercises', ('sets', 'reps', 'weight'), 'history']
    list_display = ('id','exercises')
    search_fields = ('id', 'exercises')
    list_filter = ('exercises',)
    empty_value_display = '-не указано-'


class HistoryAdmin(admin.ModelAdmin):

    fields = ['workout', 'author', 'date']
    list_display = ('id','date', 'workout', 'author')
    search_fields = ('id','date', 'workout', 'author')
    list_filter = ('id','date', 'workout', 'author')
    empty_value_display = '-не указано-'
    #inlines = [Historyline]

admin.site.register([Muscle, Tag, Hint], BaseAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(HistoryExercise, HistoryExerciseAdmin)