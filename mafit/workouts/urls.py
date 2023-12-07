from django.urls import path
from .views import ( 
     HintsListView, 
    ExerciseDetailView, 
    WorkoutDetailView,  ExerciseListView,  
    HistoryListView, WorkoutListView, 
    ExerciseCreateView, 
    WorkoutCreateView, WorkoutDeleteView, 
    WorkoutUpdateView, ExerciseDeleteView, 
    ExerciseUpdateView, manage_hist, manage_edit_hist
) 
app_name = 'workouts'

urlpatterns = [
    path('workout/<int:pk>/edit', WorkoutUpdateView.as_view(), name='workout_update'),
    path('workout/<int:pk>/delete', WorkoutDeleteView.as_view(), name='workout_delete'),
    path('workout/<int:pk>', WorkoutDetailView.as_view(), name='workout_detail'),
    path('workout/create/', WorkoutCreateView.as_view(), name='workout_create'),
    path('workout/', WorkoutListView.as_view(), name='workout_list'),

    path('history/edit/', manage_edit_hist, name='history_update'),
 #   path('history/<int:pk>/delete', HistoryDeleteView.as_view(), name='history_delete'),
    path('history/create/', manage_hist, name='history_create'),
    path('history/', HistoryListView.as_view(), name='history_list'),
    
    path('exercise/<int:pk>/edit', ExerciseUpdateView.as_view(), name='exercise_update'),
    path('exercise/<int:pk>/delete', ExerciseDeleteView.as_view(), name='exercise_delete'),
    path('exercise/<int:pk>/', ExerciseDetailView.as_view(), name='exercise_detail'),
    path('exercise/create/', ExerciseCreateView.as_view(), name='exercise_create'),
    path('exercise/', ExerciseListView.as_view(), name='exercise_list'),

    # path('hint/<int:pk>/', HintsDetailView.as_view(), name='hint_detail'),
    path('hint/', HintsListView.as_view(), name='index'),
]
