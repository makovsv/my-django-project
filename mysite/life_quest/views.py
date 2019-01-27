from django.shortcuts import render
from .forms import LifeProfileForm
from .forms import CalcForm
from .utils import *
from .models import *


def life_quest(request):

    name = "Ivan"
    form =  LifeProfileForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        nem_form1 = form.save()

    return render (request, 'life_quest/life_quest.html', locals())

def calc(request):

    form = CalcForm(request.POST or None)
    if request.method == "POST": # and form.is_valid():
        #new_form2 = form.save()
        calc_result = CalcLogic()
        v=calc_result.DoCalc()

        example=LifeProfile.objects.get(pk=10)
        example.calc_result = v
        example.save()

    return render (request, 'life_quest/calc.html', locals())
