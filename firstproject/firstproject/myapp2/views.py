from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp2.forms import StudentForm
from myapp2.models import Student
# Create your views here.
def hello(request):
	return HttpResponse('now ur in myapp2')

def register(request):
	if request.method=='POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/myapp2/register')
	form = StudentForm()
	return render(request,'myapp2/register.html',{'form':form})

def details(request):
	data = Student.objects.all()
	return render(request,'myapp2/details.html',{'data':data})

