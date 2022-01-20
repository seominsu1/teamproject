from django import forms
from .models import restaurant

class BoardForm(forms.ModelForm):
    class Meta:
        model = restaurant
        fields = ('name', 'address','phonenum','time')




