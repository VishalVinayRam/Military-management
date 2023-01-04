from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from soliders.decorators import *
from soliders.forms import MyForm,UserForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import logout


# Create your views here.
# Create your views here.
def dashboard(request):
    if not request.user.is_authenticated:
        return render(request,'/login')
    user=  User.objects.all()
        # return render(request,'dashboard.html')     
    print(user)
        
    return render(request,'dashboard.html',{'user':user})



def logouts(request):
    if request.method=="POST":
        logout(request)
        return redirect('login')


@unautheticated_user
def register_usere(request):
    if request.method == "POST":
        # username = form.cleaned_data.get('username')
        print("this is post")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print("form is valid")
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name ='general_user')
            user.groups.add(group)
            print("form is saved")
            messages.add_message(request,messages.SUCCESS,'The user is logined successfully')
            return redirect('/mains/')
        else:
            print("form is not valid")
            messages.add_message(request,messages.ERROR,'The user is not logined successfully')
            return redirect('/mains/')
    form = UserRegisterForm()
    print("logins")
    return render(request,'forms/login.html',{'form':form})


def login(request):
    if request.user.is_authenticated:
        # print()
        print("the user is auth",request.user)
        return redirect('/mains/')
    form = UserForm(request.POST)
    if request.method == "POST":
        #username = request.POST.get('username')
        print("POST")
        #data = form.objects.filter(username)
        try:
            print("trying valid")
            if form.is_valid():
                print("form is valid")
                try:
                    messages.info(request,'The user is logined successfully')
                    form.save()
                    print("form is saved")
                    return redirect('/mains/')
                except(TypeError):
                    print("error occurred1")
                    messages.add_message(request,messages.ERROR,'The user is not logined successfully')
                return redirect('/mains/')
            else:
                print("errors login")
                messages.error(request,"Login failed")
                return redirect('/mains/')


        except(e):
            messages.error(request,'Failed due to {{e}}')
            
        form = UserForm()
        print("it is only get")
        messages.add_message(request,messages.ERROR,"LOGIN FAILED")
    return render(request,'forms/login.html',{'form':form,})

def index(request):
    return render(request,"welcome.html")
