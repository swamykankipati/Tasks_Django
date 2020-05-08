from django.forms import ModelForm
from myapps.models import User

class RegisterForm(ModelForm):
	class Meta:
		model = User
		fields = ['firstName','lastName','userName','mailId','phoneNumber','age']
