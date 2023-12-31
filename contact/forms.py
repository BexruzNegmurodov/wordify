from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'number', 'email', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'name..',
        })
        self.fields['number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your number..',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your email..',
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your message..',
        })
