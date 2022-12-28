from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from soliders.forms import MyForm,UserForm
from django.contrib.auth.models import User

# Create your views here.
# Create your views here.
def solider_register(request):
    return render(request,'dashboard.html')


def register_usere(request):
    if request.method == "POST":
        username = form.cleaned_data.get('username')
        print|(username)
        if username==None:
            messages.error(request,'The user is not logined successfully')
            return redirect('/sol')
        if User.objects.filter(username=username).exists():
            messages.error(request,'The user is not logined successfully')
            return redirect('/sol')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.sucess(request,'The user is logined successfully')
            return redirect('/sol')
    else:
        form = UserCreationForm()
    return render(request,'forms/solidet_reg_form.html',{'form':form})


def login(request):
    form = UserForm(request.POST)
    if request.method == "POST":
        #username = request.POST.get('username')
        #data = form.objects.filter(username)
        if form.is_valid:
            messages.info(request,'The user is logined successfully')
            # form.save()
            return redirect('/sol/')
        form = UserForm()
    return render(request,'forms/login.html',{'form':form})

def index(request):
    return render(request,"welcome.html")
