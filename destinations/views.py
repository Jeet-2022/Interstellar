from django.shortcuts import render, redirect
from django.views.generic import DetailView
from travello.models import Destination
# Create your views here.

class DetailView(DetailView):
        model = Destination
        template_name = 'pune.html'


    
        

     
        
