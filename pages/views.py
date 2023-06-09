from django.contrib.auth.decorators import login_required

from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView

from workouts.models import Workout

from obiettivi.models import GoalModel


@login_required
def home(request):
    # Recupera il conteggio delle WORKOUT_TYPES dal modello
    user = request.user
    workout_types = []

    # Quindi, ad ogni iterazione, workout_type_display conterrà il testo leggibile dell'opzione e workout_type_value conterrà il valore effettivo dell'opzione.
    # Ad esempio, la prima iterazione restituirà ('corsa', 'Corsa').DOVE workout_type_display = 'corsa' e workout_type_value = 'Corsa'.

    for workout_type_display, workout_type_value in Workout.WORKOUT_TYPES:
        count = Workout.objects.filter(workout_type=workout_type_display, utente=user).count()
        workout_types.append((workout_type_display, count))

    workout_counts = (
        Workout.objects.filter(utente=user)
        .values('date')
        .annotate(count=Count('id'))
        .order_by('date')
    )

    counts = [entry['count'] for entry in workout_counts]
    # Converti le date in stringhe nel formato 'yyyy-mm-dd'
    dates = [entry['date'].strftime('%Y-%m-%d') for entry in workout_counts]
    completed = GoalModel.objects.filter(utente=user,is_completed=True).count()
    to_complete = GoalModel.objects.filter(utente=user,is_completed=False).count()
    all_goals = GoalModel.objects.filter(utente=user).count()

    goal = GoalModel.objects.filter(utente=user, is_selected=True).first()
    if goal is not None:
        cal_burned = goal.cal
        cal_goal = goal.CaloriesGoal
        deadline = goal.deadline
        return render(request, 'home.html', {'workout_types': workout_types, 'dates': dates, 'counts': counts,'cal_burned':cal_burned,'cal_goal':cal_goal,'is_completed':goal.is_completed,'completed':completed,'remaining':to_complete ,'deadline':deadline,'all_goals':all_goals})
    else:
        return render(request, 'home.html', {'workout_types': workout_types, 'dates': dates, 'counts': counts,'completed':completed,'remaining':to_complete,'all_goals':all_goals })