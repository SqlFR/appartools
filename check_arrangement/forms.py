from django import forms
from django.forms import ModelForm
from .models import Apartment, ApartmentIssues, IncidentType, ApartmentSheets


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['name', 'bedroom', 'bathroom']
        labels = {
            'name': "Nom de l'appartement",
            'bedroom': 'Nombre de chambre',
            'bathroom': 'Nombre de SDB'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control-input'}),
            'bedroom': forms.NumberInput(attrs={'class': 'form-control-input number-input no-arrows'}),
            'bathroom': forms.NumberInput(attrs={'class': 'form-control-input number-input no-arrows'}),
        }

    # Met la première lettre du champ 'name' en majuscule
    def clean_name(self):
        name = self.cleaned_data['name']
        return name.capitalize()


class IssuesForm(forms.ModelForm):
    class Meta:
        model = ApartmentIssues
        fields = ['room', 'incident_type', 'details']
        widgets = {
            'details': forms.Textarea(attrs={'class': 'form-control-input', 'rows': '2'})
        }

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
            # Définit dynamiquement le champ 'room' en ChoiceField
            self.fields['room'] = forms.ChoiceField(choices=rooms, label='Pièce')

    incident_type = forms.ModelChoiceField(queryset=IncidentType.objects.all(), label="Type d'incident")


# Formulaire pr la gestion des accessoires, est-ce le bon choix ?
# Je voyais ça avec un choix multiple pour chaque accessoire,
# mon idéal était une màj automatique (sans bouton submit)
class SheetForm(ModelForm):

    class Meta:
        model = ApartmentSheets
        fields = ['status']
        widgets = {
            'status': forms.Select()
        }

