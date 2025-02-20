from django import forms

class ContestForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()
    comment = forms.CharField()
