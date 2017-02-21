from .models import Activelist,Project,Client
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import forms
import datetime
from usermanagement.forms import UserForm
#encoding='utf-8'
#from .forms import ActivelistForm
# Create your views here.
def login(request):
	if request.method == 'GET':
		if request.user.is_authenticated():
#			return render(request,'activelist/index.html')
			return redirect('activelist:index')
		else:
			return render(request,'activelist/login.html')
	else:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request,user)
				return redirect('activelist:index')
			else:
				msg = 'The acount is not actived,please use another acount'
				return render(request,'activelist/login.html',{'msg':msg,'user_is_no_active':True})
		else:
			msg = 'The username or password is incorrect, please confirm'
			return render(request,'activelist/login.html',{'msg':msg,'authenticate_failed':True})

@login_required
def index(request):
	u = request.user
	activel = Activelist.objects.filter(username_id=u.id)[:50]
#	print Activelist.objects.get(username=u),'*************'
#	print '----------',u,'--------------****************'
#	print Activelist.objects.filter(username_id=u.id).values('project'),"-----------"
	return render(request,'activelist/index.html',{'activel':activel})

@login_required
def change_password(request):
	if request.method == 'GET':
		form = UserForm()
		return render(request,'activelist/change_password.html',{'form':form})
	else:
		activel = Activelist.objects.filter(username_id=request.user.id)[:50]
		usernameid = request.user.id
		user = User.objects.filter(id=usernameid).first()
		password_m = request.POST.get('password', '')
		user.set_password(password_m)
		user.save()
		return render(request,'activelist/index.html',{'user':user,'activel':activel})

@login_required
def add_active(request):
	if request.method == 'GET':
#		add_f = ActivelistForm()
		pro_m = Project.objects.all()
		cli_m = Client.objects.all()
#		print cli_m,'------------'
		tim=datetime.datetime.now().strftime('%Y-%m-%d')
		return render(request,'activelist/add.html', {'pro_m': pro_m,'cli_m': cli_m,'tim':tim})
	else:
#		add_f = Activelist(request.POST)
		usernameid = request.user.id
		user = User.objects.filter(id=usernameid).first()
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
		project=project_1,detail=detail1,username_id=usernameid)

		activel = Activelist.objects.filter(username_id=request.user.id)
		return render(request,'activelist/index.html',{'activel':activel,'user':user,'add_active':True})
#<p class="alert alert-danger">
#{{ msg }}
#</p>

@login_required
def edit_active(request,id):
	if request.method == 'GET':
#		print id,'$$$$$$$$$$$'
		active = Activelist.objects.get(id=id)
#		print active,"-----------"
		pro_m = Project.objects.all()
		cli_m = Client.objects.all()
#		print active.client,"++++++++++"
		tim = active.datetime.strftime('%Y-%m-%d')
		return render(request,'activelist/edit.html',{'active':active,'pro_m':pro_m,'cli_m':cli_m,'id':id,'tim':tim})
	else:
		username1 = request.user.id
		utype1 = request.POST.get('utype','')
		datetime1 = request.POST.get('datetime','')
		expendtime1 = request.POST.get('expendtime','')
		client1 = request.POST.get('client','')
		project1 = request.POST.get('project','')
#		print project1.encode('utf-8'),'***********'
		detail1 = request.POST.get('detail','')
		client_1 = Client.objects.get(clientl=client1)
#		client_1 = get_object_or_404(Client, client=request.POST.get['client'])
		project_1 = Project.objects.get(projectl=project1)
#		print id,'+++++++++++++++++'
		Activelist.objects.filter(id=id).update(utype=utype1,datetime=datetime1,expendtime=expendtime1,client=client_1,
		project=project_1,detail=detail1,username_id=username1)

		activel = Activelist.objects.filter(username_id=username1)
		return render(request,'activelist/index.html',{'activel':activel})

@login_required
def delete_active(request,id):
	username1 = request.user.id
	Activelist.objects.filter(id = id).delete()
	activel = Activelist.objects.filter(username_id=username1)
	return render(request,'activelist/index.html',{'activel':activel})
