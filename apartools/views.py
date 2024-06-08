from django.shortcuts import render
from django.apps import apps


def index(request):
    # Récuère l'app
    app = apps.get_app_config('check_arrangement')
    # apps_default = [
    #     'Administration', 'Authentification et autorisation',
    #     'Types de contenus', 'Sessions', 'Messages', 'Fichiers statiques', 'Liste d\'outils'
    # ]
    # # Les ajoute en excluant celles par défault
    # app_names = [app.verbose_name for app in list_apps if app.verbose_name not in apps_default]
    # app_urls = [app.url for app in list_apps if app.verbose_name not in apps_default]
    # app_names = [app.verbose_name for app in list_apps]
    # app_urls = [app.url for app in list_apps]

    context = {
        'app_name': app.verbose_name,
        'app_url': app.url,
        'app_description': app.description,
        'app_incoming': app.incoming,
    }
    return render(request, 'index.html', context)
