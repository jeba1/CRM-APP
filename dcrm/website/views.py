from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .form import SignUpForm
from .models import Employee


# Create your views here.
def home(request):
    records = Employee.objects.all()
    print(records)
    #check if user logging in
    if request.method == 'POST':
        print(request.method)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "you have logged in succesfully")
            return redirect('home')
        else: 
            messages.success(request, "please try again, error logging in")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})
  
   

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
            password = form.cleaned_data.get('password1')
            print(password)
            user = authenticate(request, username = username, password = password)
            #if user is not None:
            login(request, user)
            messages.success(request, "please try again, error logging in")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    #return render(request, 'register.html', {'form':form})
def logout_user(request):
    logout(request)
    messages.success(request, "you have been logged out...")
    return redirect('home')