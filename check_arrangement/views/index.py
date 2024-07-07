from django.shortcuts import render, redirect
from django.apps import apps

from check_arrangement.models import Apartment
from check_arrangement.forms import ApartmentForm


def index(request):
    list_apartment = Apartment.objects.filter().order_by('name')
    app = apps.get_app_config('check_arrangement')

    if request.method == 'POST':
        form = ApartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('check_arrangement:index')
    else:
        form = ApartmentForm(label_suffix='')
    context = {
        'list_apartment': list_apartment,
        'app': app,
        'form': form
    }

    return render(request, "check_arrangement/index.html", context)

