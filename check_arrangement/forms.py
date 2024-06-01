from django import forms
from .models import Apartment, ApartmentIssues, IncidentType


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['name', 'bedroom', 'bathroom']
        labels = {
            'name': "Nom de l'appartement",
            'bedroom': 'Nombre de chambres',
            'bathroom': 'Nombre de SDB'
        }


class IssuesForm(forms.ModelForm):
    class Meta:
        model = ApartmentIssues
        fields = ['room', 'incident_type', 'details']

    def __init__(self, *args, **kwargs):
        apartment = kwargs.pop('apartment', None)
        super(IssuesForm, self).__init__(*args, **kwargs)

        if apartment:
            # for i in range(1, apartment.bedroom + 1):
            #     rooms.append(f'Chambre {i}')
            #
            # for i in range(1, apartment.bathroom + 1):
            #     rooms.append(f'Salle de bain {i}')
            rooms = [('Entrée', 'Entrée'), ('Cuisine', 'Cuisine'), ('Salon', 'Salon')]
            rooms += [(f'Chambre {i}', f'Chambre {i}') for i in range(1, apartment.bedroom + 1)]
            rooms += [(f'Salle de bain {i}', f'Salle de bain {i}') for i in range(1, apartment.bathroom + 1)]
            rooms += [('Buanderie', 'Buanderie')]

            self.fields['room'] = forms.ChoiceField(choices=rooms, label='Pièce')

    incident_type = forms.ModelChoiceField(queryset=IncidentType.objects.all(), label="Type d'incident")
    details = forms.CharField(widget=forms.TextInput(attrs={'size': '40', 'max_length': '100'}), label='Détails')


