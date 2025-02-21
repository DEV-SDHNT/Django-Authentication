from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User 
from .forms import SignUpForm
import time
def loginView(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid credentials")
    return render(request,'accounts/login.html')

def signupView(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,'Account created successfully. Please log in.')
            print('Account created successfully. Please log in........')
            return redirect('login')
    else:
        form=SignUpForm()
    return render(request,'accounts/signup.html',{'form':form})

def forgotPasswordView(request):
    return render(request,'accounts/forgot_password.html')

@login_required
def changePasswordView(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"Your password is been changed successfully !")
            time.sleep(1)
            return redirect('login')
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'accounts/change_password.html',{'form':form})

@login_required
def dashboardView(request):
    return render(request,'accounts/dashboard.html')

@login_required
def profileView(request):
    return render(request,'accounts/profile.html')

def logoutView(request):
    logout(request)
    return redirect('login')   
