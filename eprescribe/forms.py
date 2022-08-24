from django.forms import ModelForm

from .models import PrescribeMed

class PrescribeForm(ModelForm):
	class Meta:
		model = PrescribeMed
		fields = '__all__'
