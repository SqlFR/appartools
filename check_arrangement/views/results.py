from django.shortcuts import get_object_or_404, redirect, render
from collections import defaultdict

from check_arrangement.models import Apartment, ApartmentSheet, ApartmentIssue


# Vue permettant de voir les incidents qui ont été ajoutés pour l'appartement sélectionné
def results(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    apartment_issues = ApartmentIssue.objects.filter(apartment_id=apartment_id)
    apartment_sheets = ApartmentSheet.objects.filter(apartment_id=apartment_id)
    status_choices = ApartmentSheet.STATUS_CHOICES

    # Initialisation du dictionnaire pour les incidents
    apartment_issues_dict = defaultdict(lambda: defaultdict(list))
    # Ajoute incidents présent dans le dict
    for issue in apartment_issues:
        room = issue.room
        issue_type = issue.issue
        details = issue.details

        apartment_issues_dict[room][issue_type].append((details, issue.id))
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
