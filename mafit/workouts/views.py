from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Hint, History, Exercise, Workout, HistoryExercise
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import  ExerciseForm, WorkoutForm, HistoryForm
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin
# class BaseView():
    
#     def __init__(self, model, request):
    
#         self._model = model
#         self.request = request # попробовать без 

#     def get_list():
        
#         model = model
#         list = model.objects.all()
#         #page_obj = paginator(request, post_list)
#         context = {'list': list}
#         #return render(request, 'posts/index.html', context)

#         pass
#     def get_detail():
#         pass
#     def create():
#         pass
#     def update():
#         pass
#     def delete():
#         pass


class HintsListView(ListView):
    model = Hint
    template_name = 'workouts/hint_list.html'


# class HintsDetailView(DetailView):
#     model = Hint
#     template_name = 'workouts/hint.html'


class WorkoutListView(ListView):
    model = Workout
    template_name = 'workouts/workout_list.html'


class WorkoutDetailView(DetailView):
    model = Workout
    template_name = 'workouts/workout.html'


class HistoryListView(ListView):
    model = HistoryExercise
    template_name = 'workouts/history_list.html'

    def get_queryset(self):
        return HistoryExercise.objects.filter(history__author=self.request.user).order_by('-history__date')
    

# class HistoryDetailView(DetailView):
#     model = History
#     template_name = 'workouts/history.html'


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


# class HistoryCreateView(CreateView):
#     pass
    # template_name = 'workouts/history_create.html'
    # model = History
    # form_class = HistoryForm
    # success_url = reverse_lazy('workouts:history_list')

from .forms import HistoryFormSet, EXFormSet
def manage_hist(request):
    
    if request.method == "POST":
        form = HistoryForm (request.POST)
        #formset = HistoryFormSet(request.POST or None)
        if form.is_valid():
            history = form.save(commit=False)
            history.author = request.user
            history = form.save()

            formset = HistoryFormSet(request.POST, instance=history)
            if formset.is_valid():
            
                formset.save()
                return redirect('workouts:history_list')
             # Do something. Should generally end with a redirect. For example:
            #return HttpResponseRedirect(author.get_absolute_url())
        form = HistoryForm ()
        formset = HistoryFormSet()
    form = HistoryForm ()
    formset = HistoryFormSet(queryset=HistoryExercise.objects.none())
    return render(request, 'workouts/history_create.html', {'form': form, 'formset': formset})


def manage_edit_hist(request):
    if request.method == 'POST':
        formset = EXFormSet(request.POST or None)
        if formset.is_valid():
            formset.save()
            return redirect('workouts:history_list')
        formset = EXFormSet(queryset=HistoryExercise.objects.filter(history__author=request.user))
    else:
        print('acho')
        formset = EXFormSet(queryset=HistoryExercise.objects.filter(history__author=request.user))
    return render(request, 'workouts/history_update.html', {'formset': formset})

# class HistoryUpdateView(UpdateView):
#     template_name = 'workouts/history_create.html'
#     model = History
#     fields = ['date', 'exercises',]
#     success_url = reverse_lazy('workouts:history_list')


# class HistoryDeleteView(DeleteView):
#     model = History
#     template_name = 'workouts/delete.html'
#     success_url = reverse_lazy('workouts:history_list')







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
    #fields = ['name', 'exercises', 'tags']
    form_class = WorkoutForm
    success_url = reverse_lazy('workouts:workout_list')


class WorkoutDeleteView(DeleteView):
    model = Workout
    template_name = 'workouts/delete.html'
    success_url = reverse_lazy('workouts:workout_list')


class ExerciseUpdateView(UpdateView):
    template_name = 'workouts/exercise_create.html'
    model = Exercise
    #fields = ['name', 'image', 'description', 'muscle']
    success_url = reverse_lazy('workouts:exercise_list')
    form_class = ExerciseForm


class ExerciseDeleteView(DeleteView):
    model = Exercise
    template_name = 'workouts/delete.html'
    success_url = reverse_lazy('workouts:exercise_list')