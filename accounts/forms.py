from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Create your models here.

class RegisterationForm(UserCreationForm):
   
    username =forms.CharField(max_length = 100,required = True, help_text ='Required' )
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address.')
    class Meta:
        model = User
    
        fields = ('username', 'email' ,'password1','password2')


class ChangeProfile(UserChangeForm):
    class Meta:
        model = User
        fields = ['username' ]
        