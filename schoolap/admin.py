from django.contrib import admin
from .models import *
# Register your models here.
class ClasAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
admin.site.register(Clas,ClasAdmin)
admin.site.register(ClasSearch)