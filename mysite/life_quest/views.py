from django.shortcuts import render
from .forms import LifeProfileForm

def life_quest(request):

    name = "Ivan"
    form =  LifeProfileForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data = form.cleaned_data
        #print (data["name"])

        nem_form1 = form.save()

    return render (request, 'life_quest/life_quest.html', locals())
