from django.shortcuts import render,redirect
from firstapp.models import *
from django.http import HttpResponse


# Create your views here.
def hi(request):
	return HttpResponse("""<h2>Hello MerC </h2>""")
# def hello(request):
# 	return HttpResponse("""<h2>Hello MerC welcome to 'Django' <h2><br> session
# 		""")
def hello(request,name):
	return HttpResponse('hii' + name + 'welocom to django')
def rollno(reg,id):
	txt = '<h2>This is ur id {} </h2>'.format(id)
	return HttpResponse(txt)
def message(request):
	return render(request,'firstApp/message.html',{})
def register(request):
	if request.method == 'POST':
		name = request.POST['uname']
		mobileno = request.POST['mbno']
		Email  = request.POST['mail']
		#print(name)
		data = {'name' : name, 'phone':mobileno,'email':Email}
		return render(request,'firstApp/details.html',{'udata': data})
		#return HttpResponse('u r successfully registered')

	return render(request, 'firstApp/register.html')

def details(request):
	dt = {'name' : 'Merc','rollno':'447'}
	return render(request,'firstApp/details.html',{'info':dt})

def registrationForm(request):

	if request.method == 'POST':
		user = 'lavanya'
		passw = '1234567890'
		Username = request.POST['Username']
		password  = request.POST['password']
		bio = {'Username' : Username , 'password' : password}
		if user == Username and passw == password :
			print('Welcome')
			return HttpResponse("""<h2>Welcome to my World</h2>""")
			
		else:
			return HttpResponse("""<h2>Oops..! Invalid credintials</h2>""")
			print("Invalid credintials")

	return render(request, 'firstApp/registrationForm.html')

def restaurantapp(request):
	if request.method == 'POST':
		biryani = request.POST['biryani']
		butternaans = request.POST['butternaans']
		biryani_cost = 220*int(biryani)
		butternaans_cost = 10*int(butternaans)
		total = biryani_cost + butternaans_cost
		menu = {'biryani' : biryani ,'butternaans' : butternaans ,'biryani_cost' : biryani_cost, 'butternaans_cost': butternaans_cost , 'total' : total }
		return render(request,'firstApp/restaurantapplication.html',{'menu': menu})
	return render(request, 'firstApp/restaurantapp.html')

def signup(request):
	if request.method =='POST':
		empid = request.POST['empid']
		empName = request.POST['empName']
		empDesign  = request.POST['empDesign']
		salary = request.POST['salary']
		obj = employee(empid = empid,empName = empName,empDesign=empDesign,salary=salary)
		obj.save()
		return redirect('/showAll')
		#return HttpResponse('Data is saved')
	return render(request,'firstApp/signup.html')


def showAll(request):
	data = employee.objects.all()
	return render(request,'firstApp/showAll.html',{'data':data})

def scboard(request):
	if request.method == 'POST':
		team1 = request.POST.get('team1')
		team2 = request.POST.get('team2')
		if team1 is not None:
			t1val = int(request.POST.get('t1val')) + 1
			t2val = int(request.POST.get('t2val'))
		else:
			t1val = int(request.POST.get('t1val'))
			t2val = int(request.POST.get('t2val'))+1
		
		scores = {'t1val':t1val,'t2val':t2val}
		return render(request,'firstApp/scboard.html',scores)

	return render(request,'firstApp/scboard.html',{})
