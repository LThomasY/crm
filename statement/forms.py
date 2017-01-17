from activelist.models import Activelist
from django.forms import ModelForm
from django import forms


class SearchForm(ModelForm,forms.Form):
    class Meta:
        model = Activelist
        fields = '__all__'
    starttime = forms.DateField()
    endtime = forms.DateField()
