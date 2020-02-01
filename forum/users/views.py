from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from rest_framework import viewsets, status
from rest_framework.authentication import (SessionAuthentication,TokenAuthentication)
from rest_framework.response import Response

class HomePageView(TemplateView):
    template_name = 'home.html'


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'