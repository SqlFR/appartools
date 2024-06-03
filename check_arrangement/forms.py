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

    # Met la première lettre du champ 'name' en majuscule
    def clean_name(self):
        name = self.cleaned_data['name']
        return name.capitalize()


class IssuesForm(forms.ModelForm):
    class Meta:
        model = ApartmentIssues
        fields = ['room', 'incident_type', 'details']

    def clean_details(self):
        details = self.cleaned_data['details']
        return details.capitalize()

    # Récupère l'instance d'appartement
    def __init__(self, *args, **kwargs):
        apartment = kwargs.pop('apartment', None)
        super(IssuesForm, self).__init__(*args, **kwargs)

        # Crée la liste rooms contenant des tuples de pièce
        if apartment:
            rooms = [('Entrée', 'Entrée'), ('Cuisine', 'Cuisine'), ('Salon', 'Salon')]
            rooms += [(f'Chambre {i}', f'Chambre {i}') for i in range(1, apartment.bedroom + 1)]
            rooms += [(f'Salle de bain {i}', f'Salle de bain {i}') for i in range(1, apartment.bathroom + 1)]
            rooms += [('Buanderie', 'Buanderie')]
            # Définit dynamiquement le champ 'roo' en ChoiceField
            self.fields['room'] = forms.ChoiceField(choices=rooms, label='Pièce')

    incident_type = forms.ModelChoiceField(queryset=IncidentType.objects.all(), label="Type d'incident")
    details = forms.CharField(widget=forms.TextInput(attrs={'size': '40', 'max_length': '100'}), label='Détails')


