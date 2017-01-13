from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Activelist(models.Model):
#    name = models.CharField(max_length=30,blank=True)
    ACT_TYPE = (
        ('per','Pre-Sales'),
        ('aft','After-Sales'),
    )
    utype = models.CharField(max_length=20,default='none',choices=ACT_TYPE)
    datetime = models.DateField()
    expendtime = models.CharField(max_length=50,default='none')
    client = models.ForeignKey('Client')
    project = models.ForeignKey('Project')
    detail = models.TextField()
#    username = models.ForeignKey('User',on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    def __unicode__(self):
        return str(self.username)
    class Meta:
        ordering = ['datetime']


class Project(models.Model):
    projectl = models.CharField(max_length=50)
    def __unicode__(self):
        return self.projectl

class Client(models.Model):
    clientl = models.CharField(max_length=50)
    def __unicode__(self):
        return self.clientl
