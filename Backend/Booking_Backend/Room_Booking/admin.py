from django.contrib import admin
from .models import Room,RoomImage,OccupiedDate
# Register your models here.
# The below line registers the Room model with the admin site 
# means that the Room model can be accessed from the admin site.
# and we can see the room modle in admin
admin.site.register(Room)
admin.site.register(RoomImage)
admin.site.register(OccupiedDate)