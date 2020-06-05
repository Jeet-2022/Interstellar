from django.shortcuts import render, redirect ,get_object_or_404
from django.views.generic import CreateView ,TemplateView ,UpdateView, View
from django.urls import reverse_lazy
from .forms import ChangeProfile
from django.views.generic.base import RedirectView 
from django.http import HttpResponse
from . import forms
from django.forms.models import BaseModelFormSet
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class RegisterationForm(CreateView):
    form_class = forms.RegisterationForm 
    template_name = 'register.html' 
    success_url = reverse_lazy('login')

    

class EditProfile(View):
    def get(self,request):
        form = forms.ChangeProfile
        return render(request,'editProfile.html',{'form': form })
    def post(self,request):
        form = forms.ChangeProfile(request.POST or None, instance = request.user)
        
        username = request.POST['username']    
        if User.objects.all().filter(username = username).exists():
                messages.info(request,'Username Taken. Please try a different username')
                return render(request,'editProfile.html',{'form': form })

        elif form.is_valid():
                    form.save()
                    return redirect(reverse_lazy('login'))                 
        else:
             form = forms.ChangeProfile(instance =request.user)

        return render(request ,'editProfile.html',{'form' : form } )

    
    
        
            
        

