from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class MyLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'name': 'username',
            'placeholder': 'name..'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'name': 'password',
            'placeholder': 'password..'
        })


class MyRegistration(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'name': 'username',
            'placeholder': 'name..'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'name': 'password1',
            'placeholder': 'password..'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'name': 'password2',
            'placeholder': 'password..'
        })
