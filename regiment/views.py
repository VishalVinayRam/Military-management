from django.shortcuts import render,redirect
from regiment.forms import RegimentForm

from regiment.models import Regiment

# Create your views here.
def regiement_logins(request):
    if request.method == "POST":
        form =  RegimentForm(request.POST)
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
        form =  RegimentForm()
    # print(form)
    return render(request,'forms/terror-register.html',{'form':form})

def dashboard(request):
    user= Regiment.objects.all()
        # return render(request,'dashboard.html')     
    print(user)
        
    return render(request,'dashboards/mission.html',{'user':user})