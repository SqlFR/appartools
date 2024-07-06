from django.shortcuts import render
from django.apps import apps

from check_arrangement.models import Apartment


def index(request):
    list_apartment = Apartment.objects.filter().order_by('name')
    app = apps.get_app_config('check_arrangement')
    context = {
        'list_apartment': list_apartment,
        'app': app
    }
    return render(request, "check_arrangement/index.html", context)
