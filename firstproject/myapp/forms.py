from django.forms import ModelForm
from myapp.models import student
class studentForm(ModelForm):
	class Meta:
		model=student
		fields='__all__'