from django import forms


class WineForm(forms.Form):
    colorint = forms.FloatField()
    proline = forms.FloatField()
