from django.apps import AppConfig


class CheckArrangementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'check_arrangement'
    verbose_name = 'Agencement d\'appart'
    description = "Renseigner les incidents sur l'appart : meubles manquants, défauts de construction ou autres."
    incoming = "Permettra le suivit de l'avancement général de l'appart."
    url = 'check-apartment/'
