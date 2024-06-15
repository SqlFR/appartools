from django.shortcuts import render, get_object_or_404, redirect
from collections import defaultdict
from .models import Apartment, ApartmentIssues
from .forms import ApartmentForm, IssuesForm
from django.apps import apps
from django.urls import reverse


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
        form = IssuesForm(request.POST, apartment=apartment)
        if form.is_valid():
            form.instance.apartment = apartment
            form.save()
            return redirect(f"{reverse('check_arrangement:add_issue', kwargs={'apartment_id': apartment.id})}?success=1")
    else:
        form = IssuesForm(apartment=apartment)
    context = {
        'apartment': apartment,
        'form': form
    }

    return render(request, 'check_arrangement/add_issue.html', context)


def results(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    apartment_issues = ApartmentIssues.objects.filter(apartment_id=apartment_id)

    # Initialisation du dictionnaire
    apartment_issues_dict = defaultdict(lambda: defaultdict(list))
    # Ajoute incidents présent dans le dict
    for issue in apartment_issues:
        room = issue.room
        incident_type = issue.incident_type
        details = issue.details

        apartment_issues_dict[room][incident_type].append((details, issue.id))
    # Conversion en dict normal
    apartment_issues_dict = {room: dict(issues) for room, issues in apartment_issues_dict.items()}

    context = {
        'apartment': apartment,
        'apartment_issues': apartment_issues,
        'apartment_issues_dict': apartment_issues_dict,
    }
    return render(request, 'check_arrangement/results.html', context)


