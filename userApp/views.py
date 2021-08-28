from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse
from userApp.models import User


class Home(TemplateView):
    template_name = "index.html"

class UserCreate(CreateView):
    template_name = "user_form.html"
    model = User

    fields = [
        "date_of_birth",
        "gender",
        "phone",
        "address",
    ]

class UserList(ListView):
    template_name = "user_list.html"
    model = User

class UserUpdate(UpdateView):
    template_name = "user_form.html"
    model = User

    fields = [
        "date_of_birth",
        "gender",
        "phone",
        "address",
    ]

class UserDelete(DeleteView):
    template_name = "user_delete.html"
    model = User

