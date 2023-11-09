from .models import *
from django import forms


class NewZakasForm(forms.ModelForm):
    class Meta:
        model = Zakas
        fields = ('product','soni',)