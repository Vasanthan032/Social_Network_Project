from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

# Create your views here.
class SignUp(CreateView):
    success_url = reverse_lazy('accounts:login')
    form_class = forms.UserCreateForm
    template_name = 'accounts/signup.html'
