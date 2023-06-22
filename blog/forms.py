from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'image', 'email', 'number', 'text')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'name...'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'image...'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'email...'
        })
        self.fields['number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'number...'
        })
        self.fields['text'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'message...'
        })
