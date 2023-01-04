from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from soliders.forms import MyForm,UserForm
from django.contrib.auth.models import User

# Create your views here.
# Create your views here.
def dashboard(request):
    user=  User.objects.all()
        # return render(request,'dashboard.html')     
    print(user)
        
    return render(request,'dashboard.html',{'user':user})


def register_usere(request):
    if request.method == "POST":
        username = form.cleaned_data.get('username')
        print|(username)
        if username==None:
            messages.error(request,'The user is not logined successfully')
            return redirect('mains')
        if User.objects.filter(username=username).exists():
            messages.error(request,'The user is not logined successfully')
            return redirect('mains')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.add_message(request,messages.SUCCESS,'The user is logined successfully')
            return redirect('mains')
    else:
        form = UserCreationForm()
    return render(request,'forms/solidet_reg_form.html',{'form':form})


def login(request):
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
