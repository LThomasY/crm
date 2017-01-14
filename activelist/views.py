from .models import Activelist,Project,Client
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django import forms
#encoding='utf-8'
#from .forms import ActivelistForm
# Create your views here.
def login(request):
	if request.method == 'GET':
		if request.user.is_authenticated():
			return render(request,'activelist/basel.html')
		else:
			return render(request,'activelist/login.html')
	else:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request,user)
				return render(request,'activelist/basel.html')
			else:
				msg = 'The acount is not actived,please use another acount'
				return render(request,'activelist/login.html',{'msg':msg,'user_is_no_active':True})
		else:
			msg = 'The username or password is incorrect, please confirm'
			return render(request,'activelist/login.html',{'msg':msg,'authenticate_failed':True})

def index(request):
	u = request.user
	activel = Activelist.objects.filter(username_id=u.id)[:10]
#	print Activelist.objects.get(username=u),'*************'
#	print '----------',u,'--------------****************'
#	print Activelist.objects.filter(username_id=u.id).values('project'),"-----------"
	return render(request,'activelist/index.html',{'activel':activel})

def add_active(request):
	if request.method == 'GET':
#		add_f = ActivelistForm()
		pro_m = Project.objects.all()
		cli_m = Client.objects.all()
#		print cli_m,'------------'
		return render(request,'activelist/add.html', {'pro_m': pro_m,'cli_m': cli_m})
	else:
#		add_f = Activelist(request.POST)
		username1 = request.user.id
		utype1 = request.POST.get('utype','')
		datetime1 = request.POST.get('datetime','')
		expendtime1 = request.POST.get('expendtime','')
		client1 = request.POST.get('client','')
		project1 = request.POST.get('project','')
#		print project1.encode('utf-8'),'***********'
		detail1 = request.POST.get('detail','')
		client_1 = Client.objects.get(clientl=client1)
		project_1 = Project.objects.get(projectl=project1)
		Activelist.objects.create(utype=utype1,datetime=datetime1,expendtime=expendtime1,client=client_1,
		project=project_1,detail=detail1,username_id=username1)
		activel = Activelist.objects.filter(username_id=request.user.id)
		return render(request,'activelist/index.html',{'activel':activel})
#<p class="alert alert-danger">
#{{ msg }}
#</p>
def edit_active(request,id):
	if request.method == 'GET':
		active = Activelist.objects.get(id=id)
		pro_m = Project.objects.all()
		cli_m = Client.objects.all()
#		print active,"++++++++++"
		return render(request,'activelist/edit.html',{'active':active,'pro_m':pro_m,'cli_m':cli_m})
	else:
		return
