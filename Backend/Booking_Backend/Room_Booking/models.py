from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class Room(models.Model): 
    #list of tuples
    ROOM_TYPES=[
        ('suite','Suite'),
        ('standard','Standard Room'),
        ("deluxe",'Deluxe Room'),
    ]
    CURRENCY_TYPES=[
        ('USD','USD'),
        ("INR",'INR'),
        ("EUR",'EUR'),      
    ]
    name=models.CharField(max_length=100,blank=True,default='')
    type=models.CharField(max_length=100,choices=ROOM_TYPES)
    currency=models.CharField(default='USD',max_length=10,choices=CURRENCY_TYPES)
    maxOccupancy=models.IntegerField(default=1)
    description=models.TextField(max_length=1000)
    pricePerNight=models.IntegerField(default=150)
   
    
    
    # It is used to the display the object in string format 
    def __str__(self):
        return f"{self.name} - {self.type} - {self.currency} - {self.maxOccupancy} - {self.description}"



class RoomImage(models.Model):
    image=models.ImageField(upload_to='room_images/')
    caption=models.CharField(max_length=200,blank=True,null=True)
    room=models.ForeignKey(Room,related_name="images",on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"Image for {self.room.name} - {self.caption or 'No Caption'}"
# foreign key is used to create a one-to-many relationship between the Room and RoomImage models.
# related_name is used to access the images of a room from the Room model.
# on_delete=models.CASCADE is used to delete the images of a room when the room is deleted.

class OccupiedDate(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE,related_name="occupiedDates")

    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="booked_dates")
    # We have created our custom User in models.py and set that in settings and now from settings importing here.
    date=models.DateField()
    
    def __str__(self):
        return f"{self.room.name} - {self.date} booked by {self.user.username}"
    
# Here bascially we are making our custom user on top of Abstract user provided bu django.

# By default django extract user by unique username or by identifying username but here we are changing by setting unique True to email
class User(AbstractUser):
    email=models.EmailField(unique=True) 
    full_name=models.CharField(max_length=100,default="")

    


