from django.shortcuts import render

def landingPage(request):
	return render(request, 'index.html', {})

def home(request):
	return render(request, 'dashboard/home.html', {})