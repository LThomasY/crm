from django.shortcuts import render
from django.contrib.auth.models import User,Group,Permission
from activelist.models import Activelist,Project,Client
from .forms import SearchForm
from django.utils import timezone
from datetime import datetime
#from django import forms
# Create your views here.
def index(request):
    u = request.user
    activel = Activelist.objects.filter(username_id=u.id)
    activeall = Activelist.objects.all()
    user = User.objects.filter(id=u.id)
#    print activel.first().username,"========="
    userl = user.first()
    return render(request,'statement/index.html',{'activel':activel,'activeall':activeall,'user':user,'userl':userl})

def search(request):
    if request.method == 'GET':
        active = SearchForm()
        pro_m = Project.objects.all()
        cli_m = Client.objects.all()
        return render(request,'statement/search.html',{'active':active,'pro_m':pro_m,'cli_m':cli_m})
    else:
        utype1 = request.POST.get('utype','')
        starttime = request.POST.get('starttime','')
        endtime = request.POST.get('endtime','')
        client1 = request.POST.get('client','')
        project1 = request.POST.get('project','')
#		print project1.encode('utf-8'),'***********'
        client_1 = Client.objects.get(clientl=client1)
        project_1 = Project.objects.get(projectl=project1)
#        str1 = '2017-1-1'
#        str2 = '2017-1-31'
#        starttime1 = datetime.strptime(starttime,'%d/%M/%Y')
#        starttime1 = datetime.date(2017, 1, 1)
#        endtime1 = datetime.date(2017, 1, 31)
#        endtime1 = datetime.strptime(str2,'%Y-%m-%d')
#        print starttime1,endtime,"**********"
        searchlist = Activelist.objects.filter(datetime__range=(starttime, endtime),utype = utype1,
        client = client_1,project = project_1)
        print searchlist,"++++++++++++"
        pro_m = Project.objects.all()
        cli_m = Client.objects.all()
        active = SearchForm()
        return render(request,'statement/search.html',{'searchlist':searchlist,'active':active,'pro_m':pro_m,'cli_m':cli_m})
