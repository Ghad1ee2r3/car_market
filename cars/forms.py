from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

        #widgets = {
        #	'opening_time': forms.TimeInput(attrs={'type':'time'}),
        #	'closing_time': forms.TimeInput(attrs={'type':'time'}),
        #}
