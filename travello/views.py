from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
from django.views.generic import ListView
# Create your views here.



class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'destination'

    def get_queryset(self):
        return Destination.objects.all()