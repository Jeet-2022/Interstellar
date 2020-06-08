from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User

# Creation of user model


class Profile(models.Model):

    user = models.OneToOneField(User,on_delete = models.CASCADE,null = True,related_name='user')
    first_name = models.CharField(max_length = 100,null = True)
    last_name = models.CharField(max_length = 100,null = True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )
    gender = models.CharField(max_length = 1, choices = GENDER_CHOICES)
    date_of_birth = models.DateField(max_length = 8)

    def __str__(self):
        return self.user.username


    





