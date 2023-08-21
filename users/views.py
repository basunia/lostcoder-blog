# from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def create_user(request):
    return render(request, "users/register.html")
