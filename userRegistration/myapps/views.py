from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapps.forms import RegisterForm
from myapps.models import User

# Create your views here.
def register(request):
	if request.method=='POST':
		password=request.POST['lastName']+'@123'
		firstName=request.POST['firstName']
		lastName=request.POST['lastName']
		userName=request.POST['userName']
		mailId=request.POST['mailId']
		phoneNumber=request.POST['phoneNumber']
		age = request.POST['age']
		form = User(firstName=firstName,lastName=lastName,userName=userName,password=password,mailId=mailId,phoneNumber=phoneNumber,age=age)
		form.save()
		# return HttpResponse('hi this is ur pwd'+password)
		return redirect('/login')
	form = RegisterForm()
	return render(request,'myApp2/register.html',{'form':form})

def login(request):
	if request.method=='POST':
		uname=request.POST['uname']
		pwd=request.POST['pwd']
		rs = User.objects.all().filter(userName=uname,password=pwd)
		print(list(rs))
		if rs:
			return render(request,'myApp2/profile.html',{'rs':rs})
			#return HttpResponse('valid user')
		return HttpResponse('not valid')
	return render(request,'myApp2/login.html',{})
