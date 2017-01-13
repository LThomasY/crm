
from .models import Activelist
from django.forms import ModelForm

class ActivelistForm(ModelForm):
    class Meta:
        model = Activelist
        fields = '__all__'
