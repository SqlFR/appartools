from django.apps import AppConfig


class CheckArrangementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'check_arrangement'
    verbose_name = 'Agencement d\'appart'
    description = ("Renseigner les incidents sur l'appart : meubles manquants, défauts de construction ou autres."
                   "Checklist de la dotation des accessoires en vue d'une livraison.")

    incoming = "Permettra le suivit plus complet de l'avancement général de l'appart."
    url = 'check-apartment/'

    def ready(self):
        import check_arrangement.signals
