from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def scoreBord(request):
	if request.method=='POST':
		team1 = request.POST.get('team1')
		team2 = request.POST.get('team2')
		if team1 is not None:
			t1val = int(request.POST.get('t1val'))+1
			t2val = int(request.POST.get('t2val'))
		else:
			t1val = int(request.POST.get('t1val'))
			t2val = int(request.POST.get('t2val')) + 1
		score = {'t1val':t1val,'t2val':t2val}
		return render(request,'firstapp/scoreBord.html',score)
	return render(request,'firstapp/scoreBord.html',{})
