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


@receiver(post_save, sender=Apartment)
def add_sheet_to_apartments(sender, created, instance, **kwargs):
    if created:
        sheets = Sheets.objects.all()
        print('Print du signal', sheets)
        for sheet in sheets:
            print('Sheet :', sheet)
            ApartmentSheets.objects.create(
                apartment=instance,
                sheet=sheet
            )
