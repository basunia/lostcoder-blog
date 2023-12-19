# from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegistrationForm


# Create your views here.
def create_user(request):
    # breakpoint()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(f'Username ${username}')
            messages.success(request, f'Account created sucessfully for {username}! Now you able to log in')
            return redirect('login')    
    else:
        form = UserRegistrationForm()
    return render(request, "users/register.html", {'form':form})

def create_login(request):
    return render(request, "users/login.html")
