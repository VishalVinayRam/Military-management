from django.shortcuts import render
from models import Family
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from soliders.models import Soliders
# Create your views here.

def Profile(request):
    if('sol_id' not in request.session):
        return redirect('/signin/')
    solider_id = request.session.get('sol_id')
    solider = Soliders.objects.get(solider_id=solider_id)
    return render(request,'Manager_Profile.html',{'solider':solider,})
    
