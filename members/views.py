from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from .forms import UserRegistrationForm

# Create your views here.
class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')



