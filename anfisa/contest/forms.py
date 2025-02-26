from django import forms

class ContestForm(forms.Form):
    title = forms.CharField(max_length=20, label='Название')
    description = forms.CharField(widget=forms.Textarea, label='Описание')
    price = forms.DecimalField(min_value=10, max_value=100, help_text='Рекомендованная розничная цена', label='Цена')
    comment = forms.CharField(widget=forms.Textarea, required=False, label='Комментарий')
