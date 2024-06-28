from django.urls import path

from .views import (ExerciseCreateView, ExerciseDeleteView, ExerciseDetailView,
                    ExerciseListView, ExerciseUpdateView, FavoritesCreateView,
                    FavoritesDeleteView, HintsListView, HistoryCreateView,
                    HistoryDetailUpdateView, HistoryDetailView,
                    HistoryListUpdateView, HistoryListView, WorkoutCreateView,
                    WorkoutDeleteView, WorkoutDetailView, WorkoutListView,
                    WorkoutUpdateView)

app_name = 'workouts'

urlpatterns = [
    path(
        'workout/<int:pk>/follow/', FavoritesCreateView.as_view(),
        name='workout_follow'
    ),
    path(
        'workout/<int:pk>/unfollow/', FavoritesDeleteView.as_view(),
        name='workout_unfollow'
    ),

    path(
        'workout/<int:pk>/edit', WorkoutUpdateView.as_view(),
        name='workout_update'
    ),
    path(
        'workout/<int:pk>/delete', WorkoutDeleteView.as_view(),
        name='workout_delete'
    ),
    path(
        'workout/<int:pk>', WorkoutDetailView.as_view(),
        name='workout_detail'
    ),
    path(
        'workout/create/', WorkoutCreateView.as_view(),
        name='workout_create'
    ),
    path(
        'workout/', WorkoutListView.as_view(),
        name='workout_list'
    ),

    path(
        'history/<int:pk>/edit', HistoryDetailUpdateView.as_view(),
        name='history_detail_update'
    ),
    path(
        'history/<int:pk>/', HistoryDetailView.as_view(),
        name='history_detail'
    ),
    path(
        'history/edit/', HistoryListUpdateView.as_view(),
        name='history_update'
    ),
    path(
        'history/create/', HistoryCreateView.as_view(),
        name='history_create'
    ),
    path(
        'history/', HistoryListView.as_view(),
        name='history_list'
    ),

    path(
        'exercise/<int:pk>/edit', ExerciseUpdateView.as_view(),
        name='exercise_update'
    ),
    path(
        'exercise/<int:pk>/delete', ExerciseDeleteView.as_view(),
        name='exercise_delete'
    ),
    path(
        'exercise/<int:pk>/', ExerciseDetailView.as_view(),
        name='exercise_detail'
    ),
    path(
        'exercise/create/', ExerciseCreateView.as_view(),
        name='exercise_create'
    ),
    path(
        'exercise/', ExerciseListView.as_view(),
        name='exercise_list'
    ),

    path('', HintsListView.as_view(), name='index'),
]
