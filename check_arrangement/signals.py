from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import IncidentType


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