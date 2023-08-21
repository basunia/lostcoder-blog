from django.urls import path
from django.urls import include
from . import views

urlpatterns = [path("", views.create_user, name="register")]
