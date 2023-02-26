from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib import messages
from soliders.decorators import *
from soliders.forms import CreateUserForm, Join_Amry_Form, Letter_form, SoliderForm, UserForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from soliders.models import Soliders
import pdfkit 
from django.contrib.auth.models import Group

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


# @unautheticated_user
# def register_usere(request):
#     if request.method == "POST":
#         # username = form.cleaned_data.get('username')
#         print("this is post")
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             print("form is valid")
#             user = form.save()
#             my_group = Group.objects.get(name='Soliders') 
#             my_group.user_set.add(user)
#             username = form.cleaned_data.get('username')
#             print("form is saved")
#             messages.add_message(request,messages.SUCCESS,'The user is logined successfully')
#             return redirect('/login/')
#         else:
#             print("form is not valid")
#             messages.error(request,"The user registraion failed")
#             # messages.add_message(request,messages.ERROR,'The user is not logined successfully')
#             return redirect('/register/')
#     form = UserRegisterForm()
#     print("logins")
#     return render(request,'forms/new_register.html',{'form':form})
    
# @unautheticated_user
def register_usere(request):
    form=CreateUserForm()
    if (request.method=="POST"):
         form=CreateUserForm(request.POST)
         if form.is_valid():
            user=form.save()
            username =form.cleaned_data.get('username')
            group=Group.objects.get(name='Soliders')
            user.groups.add(group)
            print(group)
            
            messages.success(request,'Account Created Succesfully for '+username)
            return redirect('/login')
   
    context={'form':form}
    return render(request,'forms/new_register.html',context) 

unautheticated_user
@allowed_users(allowed_roles=['Head-quarters','Recuritment'])
@login_required
def register_solider(request):
    if request.method == "POST":
        # username = form.cleaned_data.get('username')
        print("this is post")
        form = SoliderForm(request.POST)
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
    form = SoliderForm()
    print("logins")
    return render(request,'forms/terror-register.html',{'form':form,'name':'Recurit Soliders'})
def loginUser(request):
    
    if request.method=='POST':
         username=request.POST.get('username') #name in input tag
         password=request.POST.get('password')
         print(username,password)
         
         user=authenticate(request, username=username, password=password)
         print(user,"the user is none")
         if user == None:
            print("user nonoe condition")
            messages.add_message(request,messages.SUCCESS,'The user is logined successfully')
            return render(request,'forms/login.html')
         elif user is not None:
            login(request,user)
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
                print(group)
                if(group =='Solider'):
                 return redirect ('/sol/sol_mainscreen') 
                elif(group=='recuritment'):
                    return redirect ('/sol/rec_mainscreen/')
                elif(group=='Head-quarters') :
                 return redirect ('/sol/mainscreen/') 
                else:
                 return redirect ('/sol/sol_mainscreen/')
            else:
                return redirect ('/sol/sol_mainscreen/')
         else:
            messages.add_message(request,messages.WARNING,'The user is logined successfully')
            return render(request,'forms/login.html')
         
    context={}
    return render(request,'forms/login.html',context)

def index(request):
    users_in_group = Group.objects.get(name="Soliders").user_set.all()
    for i in users_in_group:
        print(i)
    return render(request,"index.html")

@allowed_users(allowed_roles=['Head-quarters','Recuritment'])
@login_required
def renders(request):
    user = Leave_Letter_Form.objects.all()
    return render(request,"dashboards/letter.html",{'user':user})

@allowed_users(allowed_roles=['Head-quarters','Recuritment'])
@login_required
def letter_confirmation(request,id):
    user = Leave_Letter_Form.objects.get(pk=id)
    user.is_approved= True
    user.save()
    return render(request,'leave_letter.html',{'i':user})



@allowed_users(allowed_roles=['Head-quarters','Admin'])
@login_required
def mainscreening(request):
    return render(request,'enter/admins.html')

@allowed_users(allowed_roles=['Recuritment','Admin'])
@login_required
def recuriment_mainscreen(request):
    return render(request,'enter/recuritment.html')


@allowed_users(allowed_roles=['Soliders','Admin'])
@login_required
def soliders_mainscreening(request):
    return render(request,'enter/soliders.html')







# @allowed_users(allowed_roles=['Solider'])
@login_required
def leave_letter(request):
    if request.method == "POST":
        form =  Letter_form(request.POST)
        datas = request.POST
        # username = datas.get('name')
        # print(words)
        if form.is_valid():
            print("HELLO")
            # messages.success(request,'The user is logined successfully')
            # print(form.cleaned_data['name'])
            form.save()
            return redirect('/sol/sol_mainscreen')
    else:        
        form =  Letter_form()
    # print(form) 
    return render(request,'forms/terror-register.html',{'form':form,'name':'Write a leave letter'})



def mainscreen(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request,'forms/leave_letetr.html')



@allowed_users(allowed_roles=['Head-quarters','Recuritment'])
@login_required
def leave_accept(request,id):
    print(id)
    user = Leave_Letter_Form.objects.get()
    user.is_approved = True
    user.save()
    pdfkit.from_file('templates/leave_letter.html','leave.pdf') 
    return render(request,'leave_letter.html',{'i':user})

def accept_army(request):
    # print(id)
    try:
        user = Join_Army.objects.get(),
        print(user)
        user.healthy = True
        user.save()
        # pdfkit.from_file('templates/leave_letter.html','leave.pdf') 
    except:
        user =None
    return render(request,'leave_letter.html',{'i':user})

def join_army(request):
    if request.method == "POST":
        form =  Join_Amry_Form(request.POST)
        datas = request.POST
        # username = datas.get('name')
        # print(words)
        if form.is_valid():
            print("HELLO")
            # messages.success(request,'The user is logined successfully')
            # print(form.cleaned_data['name'])
            form.save()
            return redirect('/sol/sol_mainscreen')
    else:        
        form =  Join_Amry_Form()
    # print(form)
    return render(request,'forms/terror-register.html',{'form':form,'name':'Join army'})
