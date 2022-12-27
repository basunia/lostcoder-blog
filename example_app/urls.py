from django.urls import path
from . import views

urlpatterns = [
    path('greeting/', views.say_hello)
]
