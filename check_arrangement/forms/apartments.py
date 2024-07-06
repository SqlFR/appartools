from django import forms

from check_arrangement.models import Apartment


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
            'bedroom': forms.NumberInput(attrs={'class': 'form-control-input number-input'}),
            'bathroom': forms.NumberInput(attrs={'class': 'form-control-input number-input'}),
        }

    # Met la première lettre du champ 'name' en majuscule
    def clean_name(self):
        name = self.cleaned_data['name']
        return name.capitalize()