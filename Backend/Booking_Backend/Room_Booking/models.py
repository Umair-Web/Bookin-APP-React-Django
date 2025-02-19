from django.db import models

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
    
     