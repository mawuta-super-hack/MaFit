from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  RedirectView, TemplateView, UpdateView, View)
from users.models import User

from .forms import ExerciseForm, HistoryForm, WorkoutForm
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
        if Favorites.objects.filter(workout_id=workout.id, user_id=self.request.user.id
                                ).exists():
            context['favorite'] = True
         

        return context


class HistoryListView(ListView):
    model = HistoryExercise
    template_name = 'workouts/history_list.html'

    def get_queryset(self):
        return HistoryExercise.objects.filter(history__author=self.request.user).order_by('-history__date')
    

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



from .forms import EXFormSet, HistoryFormSet


class HistoryCreateView(CreateView):

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:

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
        #form = HistoryForm ()
        #formset = HistoryFormSet(queryset=HistoryExercise.objects.none())
        return render(request, 'workouts/history_create.html', {'form': form, 'formset': formset})
    
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = HistoryForm ()
        formset = HistoryFormSet(queryset=HistoryExercise.objects.none())
        return render(request, 'workouts/history_create.html', {'form': form, 'formset': formset})

class HistoryListUpdateView(UpdateView):
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.method == 'POST':
            formset = EXFormSet(request.POST or None)
            if formset.is_valid():
                formset.save()
                return redirect('workouts:history_list')
            formset = EXFormSet(queryset=HistoryExercise.objects.filter(history__author=request.user))
        
        return render(request, 'workouts/history_update.html', {'formset': formset})
    
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        formset = EXFormSet(queryset=HistoryExercise.objects.filter(history__author=request.user))
        return render(request, 'workouts/history_update.html', {'formset': formset})
# def manage_hist(request):
    
#     if request.method == "POST":
#         form = HistoryForm (request.POST)
#         #formset = HistoryFormSet(request.POST or None)
#         if form.is_valid():
#             history = form.save(commit=False)
#             history.author = request.user
#             history = form.save()

#             formset = HistoryFormSet(request.POST, instance=history)
#             if formset.is_valid():
            
#                 formset.save()
#                 return redirect('workouts:history_list')
#              # Do something. Should generally end with a redirect. For example:
#             #return HttpResponseRedirect(author.get_absolute_url())
#         form = HistoryForm ()
#         formset = HistoryFormSet()
#     form = HistoryForm ()
#     formset = HistoryFormSet(queryset=HistoryExercise.objects.none())
#     return render(request, 'workouts/history_create.html', {'form': form, 'formset': formset})

class HistoryDetailView(DetailView):
    model = History
    template_name = 'workouts/history_detail.html'

class HistoryDetailUpdateView(UpdateView):
    model = History
    template_name = 'workouts/history_detail_update.html'
    form_class = HistoryForm
    

    def get_success_url(self) -> str:
        return reverse_lazy('workouts:history_detail', kwargs={'pk': self.kwargs['pk']})



def manage_edit_hist(request):
    if request.method == 'POST':
        formset = EXFormSet(request.POST or None)
        if formset.is_valid():
            formset.save()
            return redirect('workouts:history_list')
        formset = EXFormSet(queryset=HistoryExercise.objects.filter(history__author=request.user))
    else:
        
        formset = EXFormSet(queryset=HistoryExercise.objects.filter(history__author=request.user))
    return render(request, 'workouts/history_update.html', {'formset': formset})


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

    def get_success_url(self) -> str:
        return reverse_lazy('workouts:workout_detail', kwargs={'pk': self.kwargs['pk']})
    #success_url = reverse_lazy('workouts:workout_list', kwargs={'pk': self.kwargs['pk']})


class WorkoutDeleteView(DeleteView):
    model = Workout
    template_name = 'workouts/delete.html'
    success_url = reverse_lazy('workouts:workout_list')


class ExerciseUpdateView(UpdateView):
    template_name = 'workouts/exercise_create.html'
    model = Exercise
    #fields = ['name', 'image', 'description', 'muscle']
    #success_url = reverse_lazy('workouts:exercise_list')
    form_class = ExerciseForm

    def get_success_url(self) -> str:
        return reverse_lazy('workouts:exercise_detail', kwargs={'pk': self.kwargs['pk']})


class ExerciseDeleteView(DeleteView):
    model = Exercise
    template_name = 'workouts/delete.html'
    success_url = reverse_lazy('workouts:exercise_list')


# class ProfileDetailView(DetailView):
#     model = User
#     template_name = 'workouts/profile.html'
#     #pk_url_kwarg = 'user'
#     query_pk_and_slug = 'user'



# class ProfileUpdateView(UpdateView):
#     template_name = 'workouts/profile_edit.html'
#     model = User
#     #fields = ['name', 'image', 'description', 'muscle']
#     #form_class = UserWeightForm

#     def get_success_url(self):
#         pk = self.kwargs['pk']
#         return reverse_lazy('workouts:profile_detail', kwargs={'pk': pk})


class FavoritesCreateView(TemplateView):
    #template_name = 'workouts/follow.html'
    model = Favorites
    #extra_context = {'FAVORITES': True}
    
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
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
    
    #template_name = 'workouts/follow.html'
    #success_url = reverse_lazy('workouts:workout_list')

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        
        unfollow = get_object_or_404(
        Favorites,
        workout_id=self.kwargs['pk'], user_id=self.request.user.id)
        unfollow.delete()
        return redirect('workouts:workout_detail', self.kwargs['pk'])