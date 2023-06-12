from django.contrib import admin
from .models import GoalModel



class GoalAdmin(admin.ModelAdmin):
    list_display = ['utente', 'cal', 'CaloriesGoal', 'is_completed', 'is_selected', 'deadline']

admin.site.register(GoalModel, GoalAdmin)



