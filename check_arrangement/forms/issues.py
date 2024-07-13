from django import forms

from check_arrangement.models import ApartmentIssue, Issue, Apartment


# Crée la liste rooms contenant des tuples de pièce
def create_list_rooms(apartment: Apartment) -> list[tuple[str, str]]:
    rooms = [('Entrée', 'Entrée'), ('Cuisine', 'Cuisine'), ('Salon', 'Salon')]
    rooms += [(f'Chambre {i}', f'Chambre {i}') for i in range(1, apartment.bedroom + 1)]
    rooms += [(f'Salle de bain {i}', f'Salle de bain {i}') for i in range(1, apartment.bathroom + 1)]
    rooms += [('Buanderie', 'Buanderie')]

    return rooms


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

        if apartment:
            # Définit dynamiquement le champ 'room' en ChoiceField
            self.fields['room'] = forms.ChoiceField(
                choices=create_list_rooms(apartment),
                label='Pièce')

    issue = forms.ModelChoiceField(queryset=Issue.objects.all(), label="Type d'incident")


class EditIssueForm(forms.ModelForm):
    class Meta:
        model = ApartmentIssue
        fields = ['room', 'issue', 'details']
        widgets = {
            'details': forms.Textarea(attrs={'class': 'form-text-area', 'rows': '2'})
        }

    # Récupère l'instance d'appartement
    def __init__(self, *args, **kwargs):
        apartment = kwargs.pop('apartment', None)
        issue_choice_user = kwargs.pop('issue_choice_user', None)
        super(EditIssueForm, self).__init__(*args, **kwargs)

        if apartment:
            # Définit dynamiquement le champ 'room' en ChoiceField
            self.fields['room'] = forms.ChoiceField(choices=create_list_rooms(apartment), label='Pièce')
            self.fields['issue'] = forms.ModelChoiceField(queryset=Issue.objects.all(), label='Type d\'incident', initial=issue_choice_user)
    # issue = forms.ModelChoiceField(queryset=Issue.objects.all(), label="Type d'incident")

