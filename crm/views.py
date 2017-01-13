from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

def welcome(request):
	return render(request,'welcome.html')

def logout(request):
	auth_logout(request)
	return render(request,'welcome.html')
