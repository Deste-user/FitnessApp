from django.contrib import admin
from .models import CustomUser


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','birth_date','email', 'username', 'age', 'peso', 'altezza']


admin.site.register(CustomUser, UserAdmin)
