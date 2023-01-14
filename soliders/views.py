from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from soliders.decorators import *
from soliders.forms import MyForm,UserForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required

from soliders.models import Soliders


# Create your views here.
# Create your views here.
@login_required
def searching(request):
    return render(request,'forms/search.html')

@login_required
def sol_data(request):
    if not request.user.is_authenticated:
        return render(request,'/login')
    user=  Soliders.objects.all()
    for i in user:
        print(i)
    return render(request,'sol-data',{'user':user})     
    # print(user)
        
    return render(request,'sol-data.html',{'user':user})

@login_required
def dashboards(request):
    if not request.user.is_authenticated:
        return render(request,'/login')
    user=  Soliders.objects.all()
        # return render(request,'dashboard.html')     
    for i in user:
        print(i.name)   
    return render(request,'dashboards/sol-data.html',{'user':user})

def reset_password(request):
    return render(request,'forms/login.html')



def logouts(request):
    if not request.user.is_authenticated:
        return render(request,'/login')
    if request.method=="POST":
        logout(request)
        return redirect('/login')


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
    return render(request,'forms/new_register.html',{'form':form})
    
@login_required
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
    print("logins")
    return render(request,'forms/login.html',{'form':form})

# def login(request):
#     if request.user.is_authenticated:
#         # print()
#         print("the user is auth",request.user)
#         return redirect('/mains/')
#     form = UserForm(request.POST)
#     if request.method == "POST":
         
#         #username = request.POST.get('username')
#         # print("POST")
#         #data = form.objects.filter(username)
#         try:
#             if request.method=='POST':
#                 username=request.POST.get('username') #name in input tag
#                 password=request.POST.get('password')
#                 user=authenticate(request, username=username, password=password)
#             # print("trying valid")
#             # if form.is_valid():
#             #     print("form is valid")
#             #     try:
#             #         messages.info(request,'The user is logined successfully')
#             #         form.save()
#             #         print("form is saved")
#                     return redirect('/mains/')
#                 except(TypeError):
#                     print("error occurred1")
#                     messages.add_message(request,messages.ERROR,'The user is not logined successfully')
#                 return redirect('/login/')
#             else:
#                 print("errors login")
#                 messages.error(request,"Login failed")
#                 return redirect('/login/')


    #     except(e):
    #         messages.error(request,'Failed due to {{e}}')
    #     form = UserForm()
    #     print("it is only get")
    #     messages.add_message(request,messages.ERROR,"LOGIN FAILED")
    # return render(request,'forms/login.html',{'form':form,})

def loginUser(request):

      if request.method=='POST':
         username=request.POST.get('username') #name in input tag
         password=request.POST.get('password')
         print(username,password)
         
         user=authenticate(request, username=username, password=password)
         print(user)
         if user is None:
            messages.error(request,"Username not present")
            return redirect('/register')
         if user is not None:
            login(request,user)
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if(group =='solider'):
                 return redirect ('/family/data') 
            elif(group=='doctor') :
                 return redirect ('/mains') 
            else:
               return redirect('/mains')  
            
         else:
            messages.info(request,"Username or Password Incorrect")
            return render(request,'forms/login.html')
         
      context={}
      return render(request,'forms/login.html',context)

def index(request):
    return render(request,"welcome.html")


def leave_letter(request):
    return render(request,"forms/leave_letetr.html")



def mainscreen(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request,'forms/leave_letetr.html')