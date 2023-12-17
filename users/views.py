# from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib import messages


# Create your views here.
def create_user(request):
    # breakpoint()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            username = form.cleaned_data.get('username')
            print(f'Username ${username}')
            messages.success(request, f'Account created!')
            return redirect('blog-home')    
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {'form':form})

def create_login(request):
    return render(request, "users/login.html")
