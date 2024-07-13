from django.shortcuts import get_object_or_404, redirect, render
from django_ratelimit.decorators import ratelimit

from check_arrangement.models import Apartment, ApartmentSheet


# Vue pour la gestion des accessoires
def sheets(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    sheets = ApartmentSheet.objects.filter(apartment_id=apartment_id)
    sheets_not_handled = ApartmentSheet.objects.filter(apartment_id=apartment_id, status='NOT_HANDLED')
    sheets_handled = ApartmentSheet.objects.filter(apartment_id=apartment_id, status='HANDLED')
    sheets_delivery = ApartmentSheet.objects.filter(apartment_id=apartment_id, status='DELIVERY')
    sheets_unavailable = ApartmentSheet.objects.filter(apartment_id=apartment_id, status='NOT_AVAILABLE')

    all_sheets_handled = False
    # Si aucun accessoire n'est en bdd
    if not sheets_not_handled:
        all_sheets_handled = True

    context = {
     'apartment': apartment,
     'sheets':  sheets,
     'sheets_handled': sheets_handled,
     'sheets_delivery': sheets_delivery,
     'sheets_unavailable': sheets_unavailable,
     'all_sheets_handled': all_sheets_handled
    }

    return render(request, 'check_arrangement/sheets.html', context)


@ratelimit(key='ip', rate='1/s')
def to_delivery(request, apartment_id):
    sheets_handled = ApartmentSheet.objects.filter(apartment_id=apartment_id, status='HANDLED')
    sheets_handled.update(status='DELIVERY')
    return sheets(request, apartment_id)


@ratelimit(key='ip', rate='1/s')
def delivery(request, sheet_id):
    sheet = get_object_or_404(ApartmentSheet, id=sheet_id)
    sheet.status = 'DELIVERY'
    sheet.save()
    apartment_id = sheet.apartment_id

    return sheets(request, apartment_id)


@ratelimit(key='ip', rate='1/s')
def handled(request, sheet_id):
    sheet = get_object_or_404(ApartmentSheet, id=sheet_id)
    sheet.status = 'HANDLED'
    sheet.save()
    apartment_id = sheet.apartment_id

    return sheets(request, apartment_id)


@ratelimit(key='ip', rate='1/s')
def unavailable(request, sheet_id):
    sheet = get_object_or_404(ApartmentSheet, id=sheet_id)
    sheet.status = 'NOT_AVAILABLE'
    sheet.save()
    apartment_id = sheet.apartment_id

    return sheets(request, apartment_id)


@ratelimit(key='ip', rate='1/s')
def update_to_not_handled(request, apartment_sheet_handled_id):
    sheet = get_object_or_404(ApartmentSheet, id=apartment_sheet_handled_id)
    sheet.status = 'NOT_HANDLED'
    sheet.save()
    apartment_id = sheet.apartment_id
    return sheets(request, apartment_id)
