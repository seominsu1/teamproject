from django import forms
from review.models import Review

class reviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'contents')