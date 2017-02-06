from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group,Permission
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from activelist.models import Project,Client
from .forms import UserForm
# Create your views here.
@login_required
def user(request):
    users = User.objects.order_by('-id').all()
    project = Project.objects.order_by('-id').all()
    client = Client.objects.order_by('-id').all()
    return render(request,'usermanagement/user.html',{'users':users,'project':project,'client':client})

def add_project(request):
    users = User.objects.order_by('-id').all()
    client = Client.objects.order_by('-id').all()
    if request.method == 'GET':
        return render(request,'usermanagement/add_project.html')
    else:
        project_m = request.POST.get('project', '')
        Project.objects.create(projectl=project_m)
        project = Project.objects.order_by('-id').all()
        return render(request,'usermanagement/user.html',{'project':project,'users':users,'client':client})

def delete_project(request,project):
    users = User.objects.order_by('-id').all()
    client = Client.objects.order_by('-id').all()
    Project.objects.get(projectl=project).delete()
    project = Project.objects.order_by('-id').all()
    return render(request,'usermanagement/user.html',{'project':project,'users':users,'client':client})

def add_client(request):
    users = User.objects.order_by('-id').all()
    project = Project.objects.order_by('-id').all()
    if request.method == 'GET':
        return render(request,'usermanagement/add_client.html')
    else:
        client_m = request.POST.get('client', '')
        Client.objects.create(clientl=client_m)
        client = Client.objects.order_by('-id').all()
        return render(request,'usermanagement/user.html',{'client':client,'users':users,'project':project})

def delete_client(request,client):
    project = Project.objects.order_by('-id').all()
    users = User.objects.order_by('-id').all()
    Client.objects.get(clientl=client).delete()
    client = Client.objects.order_by('-id').all()
    return render(request,'usermanagement/user.html',{'client':client,'users':users,'project':project})

@login_required
def add_user(request):
    if request.method == 'GET':
        form = UserForm()
    else:
        form = UserForm(request.POST)
        project = Project.objects.order_by('-id').all()
        client = Client.objects.order_by('-id').all()
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            is_superuser = request.POST.get('is_superuser', '')
            is_staff = request.POST.get('is_staff', '')
            user = User.objects.create_user(username,email,password)
            user.first_name = phone
            user.is_active = True
            user.is_superuser = bool(is_superuser)
            user.is_staff =bool(is_staff)
            user.save()
            users = User.objects.order_by('-id').all()
            return render(request,'usermanagement/user.html',{'users':users,'project':project,'client':client,'username':username,'add_user':True})
            # return redirect('UserManagement:user')
    return render(request,'usermanagement/add_user.html',{'form': form})

def change_acount_type(request,username):
    user = User.objects.get(username=username)
    user.is_superuser = not user.is_superuser
    user.is_staff = not user.is_staff
    user.save()
    return redirect('usermanagement:user')

def reset_password(request,username):
    user = User.objects.get(username=username)
    user.set_password('yang')
    user.save()
    users = User.objects.order_by('-id').all()
    project = Project.objects.order_by('-id').all()
    client = Client.objects.order_by('-id').all()
    return render(request,'usermanagement/user.html',{'users':users,'project':project,'client':client,'username':username,'reset_password':True})

def delete_user(request,username):
    user = User.objects.get(username=username)
    user.delete()
    users = User.objects.order_by('-id').all()
    project = Project.objects.order_by('-id').all()
    client = Client.objects.order_by('-id').all()
    return render(request,'usermanagement/user.html',{'users':users,'project':project,'client':client,'username':username,'delete_user':True})
