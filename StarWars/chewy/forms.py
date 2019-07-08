from django import forms


class SearchBArForm(forms.Form):
    query = forms.CharField(max_lenght=100)
