from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=32)
    message = forms.CharField(widget=forms.Textarea)
