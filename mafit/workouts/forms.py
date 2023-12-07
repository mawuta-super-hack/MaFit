from django import forms
from .models import History, Exercise, Workout, HistoryExercise, Muscle, Tag, User
from django.forms import inlineformset_factory, formset_factory, modelformset_factory


class ExerciseForm(forms.ModelForm):

    class Meta:
        model = Exercise
        fields = ('name', 'image', 'description', 'muscle')

    muscle = forms.ModelMultipleChoiceField(
        queryset=Muscle.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class WorkoutForm(forms.ModelForm):
    #exercises = forms.MultipleChoiceField(queryset=Exercise.objects.all(),  widget=forms.CheckboxSelectMultiple)

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
    class Meta:
        model = History
        fields = ('date', 'workout')


class HistoryExerciseForm(forms.ModelForm):
    class Meta:
        model = HistoryExercise
        fields=('sets', 'reps', 'weight', 'exercises')


#HistoryFormSet = modelformset_factory(HistoryExercise, form=HistoryExerciseForm, extra=6)
HistoryFormSet = inlineformset_factory(History, HistoryExercise, form=HistoryExerciseForm, extra=6, fk_name='history')

EXFormSet = modelformset_factory(HistoryExercise, form=HistoryExerciseForm, extra=0, can_delete=True)