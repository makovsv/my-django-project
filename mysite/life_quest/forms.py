from django import forms
from .models import *

class LifeProfileForm(forms.ModelForm):

    class Meta:
        model = LifeProfile
        fields = ['myusername','birth_year','gender']
        #exclude = [""]

class CalcForm(forms.ModelForm):
    class Meta:
        model = CalcModel

        #fields = []
        exclude = [""]
