from django import forms

from check_arrangement.models import ApartmentSheet, Sheet


class EditSheetForm(forms.ModelForm):
    class Meta:
        model = ApartmentSheet
