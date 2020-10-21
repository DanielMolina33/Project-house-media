# Seller form

# Django
from django import forms


class SellerForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }),
        max_length=50,
        required=True,
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'autocomplete': 'off',
            'rows': '',
            'cols': '',
        }),
        max_length=200,
        required=True,
    )

    price = forms.CharField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }),
        required=True,
    )

    picture = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'custom-file-input',
        }),
        required=True,
    )

    tags = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'autocomplete': 'off',
            'aria-describedby': "tagsHelp",
        }),
        max_length=200,
        required=True,
    )

    classification = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'autocomplete': 'off',
            'aria-describedby': "classificationHelp",
        }),
        max_length=50,
        required=True,
    )

