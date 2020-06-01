from django.urls import path  
from django.contrib.auth import views as auth_views
 
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/',
    views.RegisterationForm.as_view(),
    name = 'register'),

    path('login/',
    auth_views.LoginView.as_view(template_name = 'login.html'),
    name = 'login'),

    path('logout/',
    auth_views.LogoutView.as_view(),
    name = 'logout'),

    path('profile/',views.EditProfile.as_view(),name ='editprofile' )
    
]