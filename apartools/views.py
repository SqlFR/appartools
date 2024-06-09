from django.shortcuts import render
from django.apps import apps


def index(request):
    # Récuère l'app
    app = apps.get_app_config('check_arrangement')

    context = {
        'app_name': app.verbose_name,
        'app_url': app.url,
        'app_description': app.description,
        'app_incoming': app.incoming,
    }
    return render(request, 'index.html', context)
