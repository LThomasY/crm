from django.shortcuts import render
from django.contrib.auth.models import User,Group,Permission
from django.contrib.auth.decorators import login_required
from activelist.models import Activelist,Project,Client
from .forms import SearchForm
from django.utils import timezone
from datetime import datetime
#from django import forms
# Create your views here.
@login_required
def index(request):
    u = request.user
    activel = Activelist.objects.filter(username_id=u.id)
    activeall = Activelist.objects.all()
    user = User.objects.filter(id=u.id).first()
#    print activel.first().username,"========="
    return render(request,'statement/index.html',{'activel':activel,'activeall':activeall,'user':user})

@login_required
def search(request):
    if request.method == 'GET':
        active = SearchForm()
        pro_m = Project.objects.all()
        cli_m = Client.objects.all()
        return render(request,'statement/search.html',{'active':active,'pro_m':pro_m,'cli_m':cli_m})
    else:
#        str1 = '2017-1-1'
#        str2 = '2017-1-31'
#        starttime1 = datetime.strptime(starttime,'%d/%M/%Y')
#        starttime1 = datetime.date(2017, 1, 1)
#        endtime1 = datetime.date(2017, 1, 31)
#        endtime1 = datetime.strptime(str2,'%Y-%m-%d')
#        print starttime1,endtime,"**********"
        user = User.objects.filter(id=request.user.id).first()

        utype1 = request.POST.get('utype','')
        print utype1,"++++++++++++++++++"
        starttime = request.POST.get('starttime','')
        endtime = request.POST.get('endtime','')
        client1 = request.POST.get('client','')
        project1 = request.POST.get('project','')
        active = SearchForm()
        pro_m = Project.objects.all()
        cli_m = Client.objects.all()
        # kwargs={}
        # if client1 != 'none':
        #     kwargs['client']= str(client1)
        #     print "------------------"
        #
        # print type(kwargs['client']),'=================='
        # searchlist = Activelist.objects.filter(**kwargs)
        # return render(request,'statement/search.html',{'searchlist':searchlist,'active':active,'pro_m':pro_m,'cli_m':cli_m})
    #    search = filter(lambda x: x,[client1,project1,utype1])
    #    if user.is_superuser:
    #        searchlist = Activelist.objects.filter(datetime__range=(starttime, endtime),search)
    #    else:
    #        searchlist = Activelist.objects.filter(username=user,datetime__range=(starttime, endtime),search)

    #    return render(request,'statement/search.html',{'searchlist':searchlist,'active':active,'pro_m':pro_m,'cli_m':cli_m})

        if (utype1 == 'none') or (client1 == 'none') or (project1 == 'none'):
            if (utype1 == 'none') and (client1 == 'none') and (project1 != 'none'):
                project_1 = Project.objects.get(projectl=project1)
                if user.is_superuser:
                    searchlist = Activelist.objects.filter(datetime__range=(starttime, endtime),project = project_1)
                else:
                    searchlist = Activelist.objects.filter(username=user,datetime__range=(starttime, endtime),project = project_1)
                return render(request,'statement/search.html',{'searchlist':searchlist,'active':active,'pro_m':pro_m,'cli_m':cli_m})

            elif (utype1 == 'none') and (client1 != 'none') and (project1 == 'none'):
                client_1 = Client.objects.get(clientl=client1)
                if user.is_superuser:
                    searchlist = Activelist.objects.filter(datetime__range=(starttime, endtime),client = client_1)
                else:
                    searchlist = Activelist.objects.filter(username=user,datetime__range=(starttime, endtime),client = client_1)
                return render(request,'statement/search.html',{'searchlist':searchlist,'active':active,'pro_m':pro_m,'cli_m':cli_m})

            elif (utype1 !=  'none') and (client1 == 'none') and (project1 == 'none'):
                if user.is_superuser:
                    searchlist = Activelist.objects.filter(datetime__range=(starttime, endtime),utype = utype1)
                else:
                    searchlist = Activelist.objects.filter(username=user,datetime__range=(starttime, endtime),utype = utype1)
                return render(request,'statement/search.html',{'searchlist':searchlist,'active':active,'pro_m':pro_m,'cli_m':cli_m})

            elif (utype1 != 'none') and (client1 != 'none') and (project1 == 'none'):
                client_1 = Client.objects.get(clientl=client1)
                if user.is_superuser:
                    searchlist = Activelist.objects.filter(datetime__range=(starttime, endtime),utype = utype1,client = client_1)
                else:
                    searchlist = Activelist.objects.filter(username=user,datetime__range=(starttime, endtime),utype = utype1,client = client_1)
                return render(request,'statement/search.html',{'searchlist':searchlist,'active':active,'pro_m':pro_m,'cli_m':cli_m})

            elif (utype1 != 'none') and (client1 == 'none') and (project1 != 'none'):
                project_1 = Project.objects.get(projectl=project1)
                if user.is_superuser:
                    searchlist = Activelist.objects.filter(datetime__range=(starttime, endtime),utype = utype1,project = project_1)
                else:
                    searchlist = Activelist.objects.filter(username=user,datetime__range=(starttime, endtime),utype = utype1,project = project_1)
                return render(request,'statement/search.html',{'searchlist':searchlist,'active':active,'pro_m':pro_m,'cli_m':cli_m})

            elif (utype1 == 'none') and (client1 != 'none') and (project1 != 'none'):
                client_1 = Client.objects.get(clientl=client1)
                project_1 = Project.objects.get(projectl=project1)
                if user.is_superuser:
                    searchlist = Activelist.objects.filter(datetime__range=(starttime, endtime),client = client_1,project = project_1)
                else:
                    searchlist = Activelist.objects.filter(username=user,datetime__range=(starttime, endtime),client = client_1,project = project_1)
                return render(request,'statement/search.html',{'searchlist':searchlist,'active':active,'pro_m':pro_m,'cli_m':cli_m})
            else:
                if user.is_superuser:
                    searchlist = Activelist.objects.filter(datetime__range=(starttime, endtime))
                else:
                    searchlist = Activelist.objects.filter(username=user,datetime__range=(starttime, endtime))
                return render(request,'statement/search.html',{'searchlist':searchlist,'active':active,'pro_m':pro_m,'cli_m':cli_m})
        else:
            client_1 = Client.objects.get(clientl=client1)
            project_1 = Project.objects.get(projectl=project1)
            if user.is_superuser:
                searchlist = Activelist.objects.filter(datetime__range=(starttime, endtime),utype = utype1,
                client = client_1,project = project_1)
            else:
                searchlist = Activelist.objects.filter(username=user,datetime__range=(starttime, endtime))
#            print searchlist,"++++++++++++"
            return render(request,'statement/search.html',{'searchlist':searchlist,'active':active,'pro_m':pro_m,'cli_m':cli_m})
