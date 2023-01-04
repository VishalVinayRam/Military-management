from django.shortcuts import render,redirect
from django.contrib import messages
from soliders.decorators import allowed_users

from terror.models import Terrorist 
from .forms import TerrorstForm



# Create your views here.
@allowed_users(allowed_roles=['Head-quarters'])
def terror_login(request):
    print(allowed_users)
    if request.method == "POST":
        form = TerrorstForm(request.POST)
        datas = request.POST
        # username = datas.get('name')
        # print(words)
        if form.is_valid():
            print("HELLO")
            messages.success(request,'The user is logined successfully')
            print(form.cleaned_data['name'])
            form.save()
            return redirect('/mains/')
    else:        
        form = TerrorstForm()
    # print(form)
    return render(request,'forms/terror-register.html',{'form':form})


def dashboard(request):
    user= Terrorist.objects.all()
        # return render(request,'dashboard.html')     
    print(user)
        
    return render(request,'dashboards/terror_data.html',{'user':user})
