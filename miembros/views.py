from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import RegistroForm

class UserRegisterView(generic.CreateView):
    model = User
    form_class = RegistroForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


