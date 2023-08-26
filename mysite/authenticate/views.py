from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm,EditProfileForm

# Create your views here.
def home(request):
    return render(request,'authenticate/home.html',{})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request,('You Have Been Logged In!'))
            return redirect('home')
        else:
            messages.success(request,('Error Logging In - Please Try Again..'))
            return redirect('login')
     
    else:
        return render(request,'authenticate/login.html',{})
    

def logout_user(request):
    logout(request)
    messages.success(request,('You Have Been Logged Out!'))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            #user=form.save()
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password = password)
            login(request,user)
            messages.success(request,('You Have Been Registered!'))
            return redirect('home')
        
    
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request,'authenticate/register.html',context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            #user=form.save()
            form.save()
            messages.success(request,('You Have Been Editted Your Profile!'))
            return redirect('home')
        
    
    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form}
    return render(request,'authenticate/edit_profile.html',context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            #user=form.save()
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,('You Have Been Updated Your Password!'))
            return redirect('home')
        
    
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request,'authenticate/change_password.html',context)
    

