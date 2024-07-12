from django.shortcuts import render, redirect
from django.apps import apps
from django.core.mail import send_mail

from check_arrangement.models import Apartment
from check_arrangement.forms import ApartmentForm, ContactForm


def index(request):
    list_apartment = Apartment.objects.filter().order_by('name')
    app = apps.get_app_config('check_arrangement')

    if request.method == 'POST':
        form = ApartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('check_arrangement:index')

        form_contact = ContactForm(request.POST)
        if form_contact.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']

            send_mail(
                subject=f'Message provenant de {name}',
                message=message,
                from_email=None,
                recipient_list=['florian.lazzarini@gmail.com']
            )

    else:
        form = ApartmentForm(label_suffix='')
        form_contact = ContactForm(label_suffix='')

    context = {
        'list_apartment': list_apartment,
        'app': app,
        'form': form,
        'form_contact': form_contact
    }

    return render(request, "check_arrangement/index.html", context)

