from django.shortcuts import render
from django.apps import apps


def index(request):
    # Récuère toutes les apps
    list_apps = apps.get_app_configs()
    apps_default = [
        'Administration', 'Authentification et autorisation',
        'Types de contenus', 'Sessions', 'Messages', 'Fichiers statiques'
    ]
    # Les ajoute en excluant celles par défault
    app_names = [app.verbose_name for app in list_apps if app.verbose_name not in apps_default]
    app_urls = [app.url for app in list_apps if app.verbose_name not in apps_default]

    context = {
        'app_names': app_names,
        'app_urls': app_urls
    }
    return render(request, 'index.html', context)
