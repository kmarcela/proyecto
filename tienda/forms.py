from django import forms
from .models import venta

class Pubform(forms.ModelForm):

    class Meta:
        model = venta
        fields = ('producto', 'precio',)
