from django.db import models

# Create your models here.
class Room(models.Model):
    ROOM_TYPES=[
        ('suite','Suite'),
        ('standard','Standard Room'),
    ]
    name=models.CharField(max_length=100,blank=True,default='')
    
     
     