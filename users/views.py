from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required 
# Create your views here.
def register(request):
    if request.method == 'POST':
        reg_form = UserRegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            messages.success(request, 'Registration Successfully')
            return redirect('users:login')
    else:
        reg_form = UserRegistrationForm()
    context = {
        'reg_form' : reg_form,
    }
    return render(request, 'user/register.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users:dashboard')
        else:
            messages.error(request, 'Username or password Invalid')
    return render(request, 'user/login.html')


@login_required(login_url='/user/login/')
def dashboard(request):
    return render(request, 'user/dashboard.html')


def user_logout(request):
    logout(request)
    return redirect('user:login')