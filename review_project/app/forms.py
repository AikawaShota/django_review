from django import forms


class SalaryForm(forms.Form):
    wage = forms.IntegerField()
    time = forms.IntegerField()
