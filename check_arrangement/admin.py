from django.contrib import admin
from .models import Apartment, IncidentType, Sheets


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'bedroom', 'bathroom')
    search_fields = ['name']
    # filter_horizontal = ['sheets']

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'name':
            formfield.label = 'Nom de l\'appartement'
        elif db_field.name == 'bedroom':
            formfield.label = 'Nombre de chambres'
        elif db_field.name == 'bathroom':
            formfield.label = 'Nombre de SDB'
        elif db_field.name == 'kitchen':
            formfield.label = 'Nombre de cuisines'
        return formfield


@admin.register(IncidentType)
class IssuesTypeAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'name':
            formfield.label = 'Nature de l\'incident'
        return formfield


@admin.register(Sheets)
class SheetsTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'room')
    list_filter = ['room']
    search_fields = ['name']


