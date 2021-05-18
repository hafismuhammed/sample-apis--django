from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import RegisterForm, LoginForm



class RegisterUserView(generic.CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'register_user.html'



