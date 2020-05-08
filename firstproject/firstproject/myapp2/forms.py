from django.forms import ModelForm

from myapp2.models import Student

class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields = '__all__'#['stuid','stuName','branch','age']