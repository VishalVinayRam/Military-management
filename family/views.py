from django.shortcuts import render
from .models import Family
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from soliders.models import *  
from soliders.decorators import *
# Create your views here.
from .forms import RegimentForm
from django.contrib.auth.decorators import login_required


def Profile(request):
    if('sol_id' not in request.session):
        return redirect('/signin/')
    solider_id = request.session.get('sol_id')
    solider = Soliders.objects.get(solider_id=solider_id)
    return render(request,'Manager_Profile.html',{'solider':solider,})
    
@allowed_users(allowed_roles=['Head-quarters','Recuritment','Solider'])
@login_required
def regiement_logins(request):
    if request.method == "POST":
        form =  Family(request.POST)
        datas = request.POST
        # username = datas.get('name')
        # print(words)
        if form.is_valid():
            print("HELLO")
            # messages.success(request,'The user is logined successfully')
            # print(form.cleaned_data['name'])
            form.save()
            return redirect('/mains/')
    else:        
        form =  Family()
    # print(form)
    return render(request,'forms/terror-register.html',{'form':form})
@login_required
def dashboard(request):
    user= Family.objects.all()
        # return render(request,'dashboard.html')     
    print(user)
        
    return render(request,'dashboards/family-data.html',{'user':user})