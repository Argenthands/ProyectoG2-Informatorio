from django import forms
from .models import Autoevaluaciones


class AutoevaluacionForm(forms.ModelForm):

	class Meta:
		model = Autoevaluaciones
		fields = '__all__'
		widgets = { '__all__': forms.RadioSelect }