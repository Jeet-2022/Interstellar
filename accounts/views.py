from django.shortcuts import render, redirect 
from django.views.generic import CreateView ,TemplateView 
from django.urls import reverse_lazy
from . import forms
from django.views.generic.base import RedirectView ,View
from django.contrib import auth
from django.http import HttpResponse

class RegisterationForm(CreateView):
    form_class = forms.RegisterationForm 
    template_name = 'register.html' 
    success_url = reverse_lazy('login')



    
    

    
        
            
        

