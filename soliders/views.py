from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from soliders.decorators import *
from soliders.forms import MyForm,UserForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import logout

from soliders.models import Soliders


# Create your views here.
# Create your views here.

def searching(request):
    return render(request,'forms/search.html')

def sol_data(request):
    if not request.user.is_authenticated:
        return render(request,'/login')
    user=  User.objects.all()
        # return render(request,'dashboard.html')     
    print(user)
        
    return render(request,'sol-data.html',{'user':user})


def dashboards(request):
    if not request.user.is_authenticated:
        return render(request,'/login')
    user=  Soliders.objects.all()
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
            print("form is saved")
            messages.add_message(request,messages.SUCCESS,'The user is logined successfully')
            return redirect('/login/')
        else:
            print("form is not valid")
            messages.error(request,"The user registraion failed")
            # messages.add_message(request,messages.ERROR,'The user is not logined successfully')
            return redirect('/register/')
    form = UserRegisterForm()
    print("logins")
    return render(request,'forms/login.html',{'form':form})

def register_solider(request):
    if request.method == "POST":
        # username = form.cleaned_data.get('username')
        print("this is post")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print("form is valid")
            user = form.save()
            username = form.cleaned_data.get('username')
            print("form is saved")
            messages.add_message(request,messages.SUCCESS,'The user is logined successfully')
            return redirect('/login/')
        else:
            print("form is not valid")
            messages.error(request,"The user registraion failed")
            # messages.add_message(request,messages.ERROR,'The user is not logined successfully')
            return redirect('/register/')
    form = USol()
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
                return redirect('/login/')
            else:
                print("errors login")
                messages.error(request,"Login failed")
                return redirect('/login/')


        except(e):
            messages.error(request,'Failed due to {{e}}')
        form = UserForm()
        print("it is only get")
        messages.add_message(request,messages.ERROR,"LOGIN FAILED")
    return render(request,'forms/login.html',{'form':form,})

def index(request):
    return render(request,"welcome.html")


def leave_letter(request):
    return render(request,"forms/leave_letter.html")