from django.shortcuts import render, redirect


from check_arrangement.models import Apartment


def delete_apartment(request, apartment_id):
    apartment = Apartment.objects.get(id=apartment_id)
    apartment.delete()
    return render('check_arrangement/index.html')
