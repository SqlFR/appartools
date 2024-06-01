from django.contrib import admin
from .models import Apartment, IncidentType


class ApartmentAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'name':
            formfield.label = 'Nom de l\'appartement'
        elif db_field.name == 'slug':
            formfield.label = 'Slug'
        elif db_field.name == 'bedroom':
            formfield.label = 'Nombre de chambres'
        elif db_field.name == 'bathroom':
            formfield.label = 'Nombre de SDB'
        return formfield

    exclude = ('slug',)  # Exclure le champ slug de l'affichage panel admin


admin.site.register(Apartment, ApartmentAdmin)


class IssuesTypeAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'name':
            formfield.label = 'Nature de l\'incident'
        return formfield


admin.site.register(IncidentType, IssuesTypeAdmin)


