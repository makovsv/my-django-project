from django import forms
from .models import *

class LifeProfileForm(forms.ModelForm):

    class Meta:
        model = LifeProfile
        fields = ['myusername']
        #exclude = [""]
