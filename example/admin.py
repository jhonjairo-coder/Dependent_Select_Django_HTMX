from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

@admin.register(Country)
class CountryModelAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')

@admin.register(City)
class CityModelAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'country')