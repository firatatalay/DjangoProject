from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Arama', max_length=100)