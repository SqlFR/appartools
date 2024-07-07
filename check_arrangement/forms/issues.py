from django import forms

from check_arrangement.models import ApartmentIssue, Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = ApartmentIssue
        fields = ['room', 'issue', 'details']
        widgets = {
            'details': forms.Textarea(attrs={'class': 'form-text-area', 'rows': '2'})
        }

    def clean_details(self):
        details = self.cleaned_data['details']
        return details.capitalize()

    # Récupère l'instance d'appartement
    def __init__(self, *args, **kwargs):
        apartment = kwargs.pop('apartment', None)
        super(IssueForm, self).__init__(*args, **kwargs)

        # Crée la liste rooms contenant des tuples de pièce
        if apartment:
            rooms = [('Entrée', 'Entrée'), ('Cuisine', 'Cuisine'), ('Salon', 'Salon')]
            rooms += [(f'Chambre {i}', f'Chambre {i}') for i in range(1, apartment.bedroom + 1)]
            rooms += [(f'Salle de bain {i}', f'Salle de bain {i}') for i in range(1, apartment.bathroom + 1)]
            rooms += [('Buanderie', 'Buanderie')]
            # Définit dynamiquement le champ 'room' en ChoiceField
            self.fields['room'] = forms.ChoiceField(choices=rooms, label='Pièce')

    issue = forms.ModelChoiceField(queryset=Issue.objects.all(), label="Type d'incident")