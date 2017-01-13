from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from .models import Activelist,Project,Client

#admin.site.register(User)
admin.site.register(Activelist)
admin.site.register(Project)
admin.site.register(Client)
