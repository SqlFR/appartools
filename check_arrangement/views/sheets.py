from django.shortcuts import get_object_or_404, redirect, render

from check_arrangement.models import Apartment, Sheet, ApartmentSheet


# Vue pour la gestion des accessoires
def sheets(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    sheets = ApartmentSheet.objects.filter(apartment_id=apartment_id)
    sheets_not_handled = ApartmentSheet.objects.filter(apartment_id=apartment_id, status='NOT_HANDLED')
    sheets_handled = ApartmentSheet.objects.filter(apartment_id=apartment_id, status='HANDLED')
    sheets_delivery = ApartmentSheet.objects.filter(apartment_id=apartment_id, status='DELIVERY')
    sheets_unavailable = ApartmentSheet.objects.filter(apartment_id=apartment_id, status='NOT_AVAILABLE')

    all_sheets_handled = False

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


def to_delivery(request, apartment_id):
    sheets_handled = ApartmentSheet.objects.filter(apartment_id=apartment_id, status='HANDLED')
    sheets_handled.update(status='DELIVERY')
    return redirect('check_arrangement:sheets', apartment_id=apartment_id)


def delivery(request, sheet_id):
    sheet = ApartmentSheet.objects.filter(id=sheet_id)
    apartment_id = sheet.values()[0]['apartment_id']
    sheet.update(status='DELIVERY')
    return redirect('check_arrangement:sheets', apartment_id=apartment_id)


def handled(request, sheet_id):
    sheet = ApartmentSheet.objects.filter(id=sheet_id)
    apartment_id = sheet.values()[0]['apartment_id']
    sheet.update(status='HANDLED')
    return redirect('check_arrangement:sheets', apartment_id=apartment_id)


def unavailable(request, sheet_id):
    sheet = ApartmentSheet.objects.filter(id=sheet_id)
    apartment_id = sheet.values()[0]['apartment_id']
    sheet.update(status='NOT_AVAILABLE')
    return redirect('check_arrangement:sheets', apartment_id=apartment_id)


def update_to_not_handled(request, apartment_sheet_handled_id):
    apartment_sheet_handled = ApartmentSheet.objects.filter(id=apartment_sheet_handled_id)
    apartment_id = apartment_sheet_handled.values()[0]['apartment_id']  # Recup l'id de l'appart
    apartment_sheet_handled.update(status='NOT_HANDLED')
    return redirect('check_arrangement:sheets', apartment_id=apartment_id)