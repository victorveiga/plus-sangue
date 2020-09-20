from django.contrib import admin
from .models import Doador
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Doador)
class DoadorAdmin(ImportExportModelAdmin):
    pass