from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.forms import studentForm
# Create your views here.
def hello(reqest):
	return HttpResponse('hello this is 2project myapp')

def register(request):
	if request=="POST":
		form = studentForm(request.POST)
		form.save()
		return redirect('/myapp/register')
	form = studentForm()
	return render(request,'myapp/register.html',{'form':form})

def details(request):
	data = student.objects.all()
	return render(request,'myapp/details.html',{'data':data})