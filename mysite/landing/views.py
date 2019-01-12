from django.shortcuts import render

def landing(request):
    name = "Ivan"
    return render (request, 'landing/landing.html', locals())
