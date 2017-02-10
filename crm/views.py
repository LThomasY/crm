from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
# Create your views here.

def welcome(request):
	#return render(request,'activelist/login.html')
	return redirect('activelist:login')
def logout(request):
	auth_logout(request)
	return render(request,'activelist/login.html')
