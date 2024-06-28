QUERY_HINTS = 'SELECT * FROM workouts_hint;'

QUERY_FILTER_TAGS = (
    'SELECT DISTINCT workouts_tag.name FROM workouts_workout'
    + ' JOIN workouts_workout_tags ON workouts_workout_tags.workout_id=workouts_workout.id'
    + ' JOIN workouts_tag ON workouts_tag.id = workouts_workout_tags.tag_id'
)
QUERY_FILTER_MUSCLE = (
    'SELECT DISTINCT workouts_muscle.name FROM workouts_exercise'
    + ' JOIN workouts_exercise_muscle ON workouts_exercise_muscle.exercise_id=workouts_exercise.id'
    + ' JOIN workouts_muscle ON workouts_muscle.id = workouts_exercise_muscle.muscle_id'
)

QUERY_FILTER_WORKOUTS = (
    'SELECT workouts_workout.name, workouts_tag.name FROM workouts_workout'
    + ' JOIN workouts_workout_tags ON workouts_workout_tags.workout_id=workouts_workout.id'
    + ' JOIN workouts_tag ON workouts_tag.id = workouts_workout_tags.tag_id'
    + ' WHERE workouts_tag.name=\'CALL\';'
)
QUERY_FILTER_EXERCISE = (
    'SELECT workouts_exercise.name, workouts_muscle.name FROM workouts_exercise'
    + ' JOIN workouts_exercise_muscle ON workouts_exercise_muscle.exercise_id=workouts_exercise.id'
    + ' JOIN workouts_muscle ON workouts_muscle.id = workouts_exercise_muscle.muscle_id'
    + ' WHERE workouts_muscle.name=\'CALL\';'
)
QUERY_RESULT_WORKOUTS = (
    'SELECT  workouts_exercise.image, workouts_exercise.name, workouts_exercise.description FROM workouts_workout'
    + ' JOIN workouts_workout_exercises ON workouts_workout_exercises.workout_id=workouts_workout.id'
    + ' JOIN workouts_exercise ON workouts_exercise.id = workouts_workout_exercises.exercise_id'
    + ' WHERE workouts_workout.name=\'CALL\';'
)
QUERY_RESULT_EXERCISE = (
    'SELECT workouts_exercise.image, workouts_exercise.name, workouts_exercise.description FROM workouts_exercise'
    + ' JOIN workouts_exercise_muscle ON workouts_exercise_muscle.exercise_id=workouts_exercise.id'
    + ' JOIN workouts_muscle ON workouts_muscle.id = workouts_exercise_muscle.muscle_id'
    + ' WHERE workouts_exercise.name=\'CALL\';'
)
