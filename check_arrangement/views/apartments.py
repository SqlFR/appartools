from django.shortcuts import render, redirect

from check_arrangement.forms import ApartmentForm
from check_arrangement.models import Apartment


def add_apartment(request):
    if request.method == 'POST':
        form = ApartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('check_arrangement:index')
    else:
        form = ApartmentForm()
    return render(request, 'check_arrangement/add_apartment.html', {'form': form})


def delete_apartment(request, apartment_id):
    apartment = Apartment.objects.get(id=apartment_id)
    apartment.delete()
    return redirect('check_arrangement:index')