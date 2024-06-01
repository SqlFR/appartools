from django.apps import AppConfig


class CheckArrangementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'check_arrangement'
    verbose_name = 'Vérif appartement'
    url = 'check-apartment/'
