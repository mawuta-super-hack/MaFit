from typing import Any

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)
from users.models import User

from .forms import (ExerciseForm, HistoryForm, WorkoutForm,
                    EXFormSet, HistoryFormSet)
from .models import (Exercise, Favorites, Hint, History, HistoryExercise,
                     Workout)


class HintsListView(ListView):
    model = Hint
    template_name = 'workouts/hint_list.html'


class WorkoutListView(ListView):
    model = Workout
    template_name = 'workouts/workout_list.html'


class WorkoutDetailView(DetailView):
    model = Workout
    template_name = 'workouts/workout.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        workout = get_object_or_404(Workout, pk=self.kwargs['pk'])
        if Favorites.objects.filter(
                workout_id=workout.id, user_id=self.request.user.id).exists():
            context['favorite'] = True
        return context


class WorkoutCreateView(CreateView):
    template_name = 'workouts/workout_create.html'
    model = Workout
    form_class = WorkoutForm
    success_url = reverse_lazy('workouts:workout_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(WorkoutCreateView, self).form_valid(form)


class WorkoutUpdateView(UpdateView):
    template_name = 'workouts/workout_create.html'
    model = Workout
    form_class = WorkoutForm

    def get_success_url(self) -> str:
        return reverse_lazy(
            'workouts:workout_detail', kwargs={'pk': self.kwargs['pk']}
        )


class WorkoutDeleteView(DeleteView):
    model = Workout
    template_name = 'workouts/delete.html'
    success_url = reverse_lazy('workouts:workout_list')


class ExerciseListView(ListView):
    model = Exercise
    template_name = 'workouts/exercise_list.html'


class ExerciseDetailView(DetailView):
    model = Exercise
    template_name = 'workouts/exercise.html'


class ExerciseCreateView(CreateView):
    template_name = 'workouts/exercise_create.html'
    model = Exercise
    form_class = ExerciseForm
    success_url = reverse_lazy('workouts:exercise_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ExerciseCreateView, self).form_valid(form)


class ExerciseUpdateView(UpdateView):
    template_name = 'workouts/exercise_create.html'
    model = Exercise
    form_class = ExerciseForm

    def get_success_url(self) -> str:
        return reverse_lazy(
            'workouts:exercise_detail', kwargs={'pk': self.kwargs['pk']}
        )


class ExerciseDeleteView(DeleteView):
    model = Exercise
    template_name = 'workouts/delete.html'
    success_url = reverse_lazy('workouts:exercise_list')


class HistoryListView(ListView):
    model = HistoryExercise
    template_name = 'workouts/history_list.html'

    def get_queryset(self):
        return HistoryExercise.objects.filter(
            history__author=self.request.user
        ).order_by('-history__date')


class HistoryCreateView(CreateView):

    def post(self, request):
        form = HistoryForm(request.POST)
        if form.is_valid():
            history = form.save(commit=False)
            history.author = request.user
            history = form.save()
            formset = HistoryFormSet(request.POST, instance=history)
            if formset.is_valid():
                formset.save()
                return redirect('workouts:history_list')
        form = HistoryForm()
        formset = HistoryFormSet()
        return render(
            request, 'workouts/history_create.html',
            {'form': form, 'formset': formset}
        )

    def get(self, request):
        form = HistoryForm()
        formset = HistoryFormSet(queryset=HistoryExercise.objects.none())
        return render(
            request, 'workouts/history_create.html',
            {'form': form, 'formset': formset}
        )


class HistoryListUpdateView(UpdateView):
    def post(self, request):
        if request.method == 'POST':
            formset = EXFormSet(request.POST or None)
            if formset.is_valid():
                formset.save()
                return redirect('workouts:history_list')
            formset = EXFormSet(
                queryset=HistoryExercise.objects.filter(
                    history__author=request.user
                )
            )
        return render(
            request, 'workouts/history_update.html',
            {'formset': formset}
        )

    def get(self, request):
        formset = EXFormSet(
            queryset=HistoryExercise.objects.filter(
                history__author=request.user
            )
        )
        return render(
            request, 'workouts/history_update.html',
            {'formset': formset}
        )


class HistoryDetailView(DetailView):
    model = History
    template_name = 'workouts/history_detail.html'


class HistoryDetailUpdateView(UpdateView):
    model = History
    template_name = 'workouts/history_detail_update.html'
    form_class = HistoryForm

    def get_success_url(self) -> str:
        return reverse_lazy(
            'workouts:history_detail', kwargs={'pk': self.kwargs['pk']}
        )


class FavoritesCreateView(TemplateView):
    model = Favorites

    def get(self, request):
        pk = self.kwargs['pk']
        workout = get_object_or_404(Workout, pk=pk)
        pk = self.request.user.id
        user = get_object_or_404(User, pk=pk)
        favorite = Favorites.objects.create(
            workout_id=workout.id, user_id=user.id)
        favorite.save()
        return redirect('workouts:workout_detail', self.kwargs['pk'])


class FavoritesDeleteView(TemplateView):
    model = Favorites

    def get(self, request):
        unfollow = get_object_or_404(
            Favorites, workout_id=self.kwargs['pk'],
            user_id=self.request.user.id
        )
        unfollow.delete()
        return redirect('workouts:workout_detail', self.kwargs['pk'])
