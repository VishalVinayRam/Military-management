from django.shortcuts import render,redirect
from models import Mission



# Create your views here.
def regiement_logins(request):
    if request.method == "POST":
        form = Mission(request.POST)
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
        form = Mission()
    # print(form)
    return render(request,'forms/terror-register.html',{'form':form})
