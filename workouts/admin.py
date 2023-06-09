from django.contrib import admin

from .forms import WorkoutForm
from .models import Workout
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['date', 'calories_burned', 'workout_type','weight','repetitions' ,'descrizione','distance']

admin.site.register(Workout, WorkoutAdmin)
