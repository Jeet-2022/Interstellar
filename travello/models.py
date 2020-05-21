from django.db import models

# Create your models here.


class Destination(models.Model):    #imported SQL model from model fields

    name = models.CharField(max_length = 100)     #for character
    img = models.ImageField(upload_to = 'pics')   #for pictures
    desc = models.TextField()                     #for text
    price = models.IntegerField()                 #for integer
    offer = models.BooleanField(default = False)  #for boolean
    
