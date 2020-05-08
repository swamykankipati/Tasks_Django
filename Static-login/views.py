def registrationForm(request):

	if request.method == 'POST':
		user = 'varunswami'
		passw = '0987654321'
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