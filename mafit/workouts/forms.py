from django import forms
from django.forms import inlineformset_factory, modelformset_factory

from .models import Exercise, History, HistoryExercise, Muscle, Tag, Workout


class ExerciseForm(forms.ModelForm):

    class Meta:
        model = Exercise
        fields = ('name', 'image', 'description', 'muscle')

    muscle = forms.ModelMultipleChoiceField(
        queryset=Muscle.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class WorkoutForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = ('name', 'exercises', 'tags')

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    exercises = forms.ModelMultipleChoiceField(
        queryset=Exercise.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class HistoryForm(forms.ModelForm):

    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={"rows": 2, "cols": 100}), help_text='Комментарий')

    class Meta:
        model = History
        fields = ('date', 'workout', 'comment')


class HistoryExerciseForm(forms.ModelForm):

    class Meta:
        model = HistoryExercise
        fields = ('sets', 'reps', 'weight', 'exercises')


HistoryFormSet = inlineformset_factory(
    History, HistoryExercise,
    form=HistoryExerciseForm, extra=6, fk_name='history'
)

EXFormSet = modelformset_factory(
    HistoryExercise,
    form=HistoryExerciseForm, extra=0, can_delete=True
)
