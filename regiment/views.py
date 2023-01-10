from django.shortcuts import render,redirect
from regiment.forms import RegimentForm

from regiment.models import Regiment
from soliders.decorators import allowed_users

# Create your views here.
def searching(request):
    if request.method=='GET':
      data =request.GET.get('search')
      searching = Regiment.objects.all().filter(id=data)
      print(searching)
      user={
        'searching':searching
      }
      return render(request,'dashboards/regiment.html',{'user':user})
    if request.method =='POST':
        data =request.POST.get('search')
        searching = Regiment.objects.all().filter(regiment_id=data)
        print(searching)
        user={
            'searching':searching
        }
        return render(request,'dashboards/regiment.html',{'user':user})
    return render(request,'forms/search.html')


@allowed_users(allowed_roles=['Head-quarters'])

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
        
    return render(request,'dashboards/regiment.html',{'user':user})