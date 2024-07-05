from django.shortcuts import render, get_object_or_404, redirect
from collections import defaultdict
from .models import Apartment, ApartmentIssues, ApartmentSheets
from .forms import ApartmentForm, IssuesForm, SheetForm
from django.apps import apps
from django.urls import reverse

from . import forms


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


def delete_issue(request, apartmentissues_id):
    issue = get_object_or_404(ApartmentIssues, id=apartmentissues_id)
    issue.delete()
    return redirect('check_arrangement:results', apartment_id=issue.apartment.id)


def index(request):
    list_apartment = Apartment.objects.filter().order_by('name')
    app = apps.get_app_config('check_arrangement')
    context = {
        'list_apartment': list_apartment,
        'app': app
    }
    return render(request, "check_arrangement/index.html", context)


def add_issue(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    if request.method == 'POST':
        form = IssuesForm(request.POST, apartment=apartment,)
        rendered_form = form.render("check_arrangement/forms/form_snippet.html")
        if form.is_valid():
            form.instance.apartment = apartment
            form.save()
            return redirect(f"{reverse('check_arrangement:add_issue', kwargs={'apartment_id': apartment.id})}?success=1")
    else:
        form = IssuesForm(apartment=apartment, label_suffix='')
        rendered_form = form.render("check_arrangement/forms/form_snippet.html")
    context = {
        'apartment': apartment,
        'form': rendered_form
    }

    return render(request, 'check_arrangement/add_issue.html', context)


# Vue pour la gestion des accessoires
# Récupère chaque accessoire pour distribuer aux formulaires
def sheets(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    sheets = ApartmentSheets.objects.filter(apartment_id=apartment_id)
    sheets_not_handled = ApartmentSheets.objects.filter(apartment_id=apartment_id, status='NOT_HANDLED')
    sheets_handled = ApartmentSheets.objects.filter(apartment_id=apartment_id, status='HANDLED')
    sheets_delivery = ApartmentSheets.objects.filter(apartment_id=apartment_id, status='DELIVERY')
    sheets_unavailable = ApartmentSheets.objects.filter(apartment_id=apartment_id, status='NOT_AVAILABLE')

    all_sheets_handled = False

    if not sheets_not_handled:
        all_sheets_handled = True

    print(all_sheets_handled)
    context = {
     'apartment': apartment,
     'sheets':  sheets,
     'sheets_handled': sheets_handled,
     'sheets_delivery': sheets_delivery,
     'sheets_unavailable': sheets_unavailable,
     'all_sheets_handled': all_sheets_handled
    }

    return render(request, 'check_arrangement/sheets.html', context)


def delivery(request, sheet_id):
    sheet = ApartmentSheets.objects.filter(id=sheet_id)
    apartment_id = sheet.values()[0]['apartment_id']
    sheet.update(status='DELIVERY')
    return redirect('check_arrangement:sheets', apartment_id=apartment_id)


def handled(request, sheet_id):
    sheet = ApartmentSheets.objects.filter(id=sheet_id)
    apartment_id = sheet.values()[0]['apartment_id']
    sheet.update(status='HANDLED')
    return redirect('check_arrangement:sheets', apartment_id=apartment_id)


def unavailable(request, sheet_id):
    sheet = ApartmentSheets.objects.filter(id=sheet_id)
    apartment_id = sheet.values()[0]['apartment_id']
    sheet.update(status='NOT_AVAILABLE')
    return redirect('check_arrangement:sheets', apartment_id=apartment_id)


def to_delivery(request, apartment_id):
    sheets_handled = ApartmentSheets.objects.filter(apartment_id=apartment_id, status='HANDLED')
    sheets_handled.update(status='DELIVERY')
    return redirect('check_arrangement:sheets', apartment_id=apartment_id)


def update_to_not_handled(request, apartment_sheet_handled_id):
    apartment_sheet_handled = ApartmentSheets.objects.filter(id=apartment_sheet_handled_id)
    apartment_id = apartment_sheet_handled.values()[0]['apartment_id']  # Recup l'id de l'appart
    apartment_sheet_handled.update(status='NOT_HANDLED')
    return redirect('check_arrangement:sheets', apartment_id=apartment_id)


# Vue permettant de voir les incidents qui ont été ajoutés pour l'appartement sélectionné
def results(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    apartment_issues = ApartmentIssues.objects.filter(apartment_id=apartment_id)
    apartment_sheets = ApartmentSheets.objects.filter(apartment_id=apartment_id)
    status_choices = ApartmentSheets.STATUS_CHOICES

    # Initialisation du dictionnaire pour les incidents
    apartment_issues_dict = defaultdict(lambda: defaultdict(list))
    # Ajoute incidents présent dans le dict
    for issue in apartment_issues:
        room = issue.room
        incident_type = issue.incident_type
        details = issue.details

        apartment_issues_dict[room][incident_type].append((details, issue.id))
    # Conversion en dict normal
    apartment_issues_dict = {room: dict(issues) for room, issues in apartment_issues_dict.items()}

    apartment_sheets_dict = defaultdict(list)

    for sheet in apartment_sheets:
        apartment_sheets_dict[sheet.status].append(sheet)

    apartment_sheets_dict = dict(apartment_sheets_dict)

    apartment_sheets = {value: apartment_sheets_dict.get(key, []) for key, value in status_choices}

    context = {
        'apartment': apartment,
        'apartment_issues_dict': apartment_issues_dict,
        'apartment_sheets': apartment_sheets
    }
    return render(request, 'check_arrangement/results.html', context)


