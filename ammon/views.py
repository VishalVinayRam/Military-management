from django.shortcuts import render,redirect

from soliders.decorators import allowed_users
from .models import Ammo
from .forms import RegimentForm



# Create your views here.
@allowed_users(allowed_roles=['Head-quarters','Recuritment'])
def regiement_logins(request):
    if request.method == "POST":
        form = RegimentForm(request.POST)
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
        form = RegimentForm()
    # print(form)
    return render(request,'forms/terror-register.html',{'form':form})

def dashboard(request):
    user= Ammo.objects.all()
        # return render(request,'dashboard.html')     
    print(user)
        
    return render(request,'dashboards/ammo-data.html',{'user':user})