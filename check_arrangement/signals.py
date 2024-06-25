from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from .models import IncidentType, Apartment, Sheets, ApartmentSheets

# Ajoute les types d'incidents automatiquement (lors d'une migration)
@receiver(post_migrate)
def add_default_incident_types(sender, **kwargs):
    if sender.name == 'check_arrangement':
        default_incident_types = [
            'Article(s) manquant(s)',
            'Défault de construction',
            'Electricité',
            'Plomberie',
            'Internet',
            'Autres'
        ]

        for incident_type in default_incident_types:
            IncidentType.objects.get_or_create(name=incident_type)


# Ajoute automatiquement les accessoires (enregistré en db) à la création de l'appart
@receiver(post_save, sender=Apartment)
def add_sheets_when_apartment_created(sender, created, instance, **kwargs):
    if created:
        sheets = Sheets.objects.all()
        for sheet in sheets:
            ApartmentSheets.objects.create(
                apartment=instance,
                sheet=sheet
            )


# Ajoute l'accessoire qui vient d'être créé à tous les appartements déjà créé
@receiver(post_save, sender=Sheets)
def add_sheet_to_apartment_when_created(sender, created, instance, **kwargs):
    if created:
        apartments = Apartment.objects.all()
        for apartment in apartments:
            ApartmentSheets.objects.create(
                apartment=apartment,
                sheet=instance
            )
