from django.shortcuts import render, redirect
from django.apps import apps
from django.conf import settings
from django.core.mail import send_mail

from check_arrangement.models import Apartment
from check_arrangement.forms import ApartmentForm, ContactForm


def index(request):
    list_apartment = Apartment.objects.filter().order_by('name')
    app = apps.get_app_config('check_arrangement')

    if request.method == 'POST':
        form = ApartmentForm(request.POST, prefix='add_apart')
        form_contact = ContactForm(request.POST, prefix='contact')
        if 'add_apart_submit' in request.POST and form.is_valid():
            form.save()
            return redirect('check_arrangement:index')
        if 'contact_submit' in request.POST and form_contact.is_valid():
            name = form_contact.cleaned_data['name']
            subject = f'Message provenant de {name}'
            message = form_contact.cleaned_data['message']
            from_email = 'contact@apartools.com'
            recipient_list = ['florian.lazzarini@gmail.com']

            print('Formulaire validé')
            send_mail(subject, message, from_email, recipient_list)
        else:
            print('Formulaire non validé')

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

