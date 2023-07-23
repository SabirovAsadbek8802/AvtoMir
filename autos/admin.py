from django.contrib import admin
from .models import Autos
# Register your models here.

class AutosAdmin(admin.ModelAdmin):
    list_display = ("brand","model_auto")

admin.site.register(Autos, AutosAdmin)