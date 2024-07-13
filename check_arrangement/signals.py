from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from .models import Issue, Apartment, Sheet, ApartmentSheet


# Ajoute les types d'incidents automatiquement (lors d'une migration)
@receiver(post_migrate)
def add_default_issue(sender, **kwargs):
    if sender.name == 'check_arrangement':
        default_issue = [
            'Article(s) manquant(s)',
            'Défault de construction',
            'Electricité',
            'Plomberie',
            'Internet',
            'Autres'
        ]

        for issue in default_issue:
            Issue.objects.get_or_create(name=issue)


# Ajoute les accessoires
@receiver(post_migrate)
def add_sheets(sender, **kwargs):
    if sender.name == 'check_arrangement':
        default_sheets = {
            'KITCHEN': ('Poêles', 'Casseroles'),
            'BATHROOM': ('Tapis de de bain', 'Brosse toilettes'),
            'COMMON': 'Rack à chaussures'
        }

        for room, sheet in default_sheets.items():
            if isinstance(sheet, tuple):  # Prévient si valeur dans le dict n'est pas un tuple
                for item in sheet:
                    Sheet.objects.get_or_create(room=room, name=item)
            else:
                Sheet.objects.get_or_create(room=room, name=sheet)


# Ajoute automatiquement les accessoires (enregistré en db) à la création de l'appart
@receiver(post_save, sender=Apartment)
def add_sheets_when_apartment_created(sender, created, instance, **kwargs):
    if created:
        sheets = Sheet.objects.all()
        for sheet in sheets:
            ApartmentSheet.objects.create(
                apartment=instance,
                sheet=sheet
            )


# Ajoute l'accessoire qui vient d'être créé à tous les appartements déjà créé
@receiver(post_save, sender=Sheet)
def add_sheet_to_apartment_when_created(sender, created, instance, **kwargs):
    if created:
        apartments = Apartment.objects.all()
        for apartment in apartments:
            ApartmentSheet.objects.create(
                apartment=apartment,
                sheet=instance
            )
