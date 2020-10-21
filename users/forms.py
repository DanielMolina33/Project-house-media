# Login and Register form

# Django
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control',
        }),
        max_length=150,
        required=True,
        label=False,
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
        }),
        max_length=20,
        required=True,
        label=False,
    )


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control',
            'autocomplete': 'off',
        }),
        max_length=150,
        required=True,
        label=False,
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
        }),
        max_length=20,
        required=True,
        label=False,
    )

    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password confirmation',
            'class': 'form-control',
        }),
        max_length=20,
        required=True,
        label=False,
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'class': 'form-control',
            'autocomplete': 'off',
        }),
        max_length=150,
        required=True,
        label=False,
    )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'First name',
            'class': 'form-control',
            'autocomplete': 'off',
        }),
        max_length=150,
        required=True,
        label=False,
    )

    last_name = forms.CharField(
         widget=forms.TextInput(attrs={
            'placeholder': 'Last name',
            'class': 'form-control',
            'autocomplete': 'off',
        }),
        max_length=150,
        required=True,
        label=False,
    )

    is_seller = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            'class': 'align-middle'
        }),
        required=False,
    )
