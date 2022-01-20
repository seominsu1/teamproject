from django import forms
from .models import Review

class reviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'contents')