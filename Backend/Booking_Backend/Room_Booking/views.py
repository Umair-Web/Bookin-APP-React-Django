from django.shortcuts import render
from rest_framework import generics
# Generics DRF me pre-built views hain jo CRUD (Create, Read, Update, Delete) operations
# ko aasaan aur efficient banati hain. Yeh views reusable hote hain aur kam code likhne me madad dete hain.


from .models import Room
from .serializers import RoomSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
# Yeh decorator hai jo function-based views ko API view banata hai. 
# Isko use karne ka maqsad request methods (GET, POST, etc.) define karna hota hai

# Yeh DRF ka custom response object hai jo JSON format me response return karta hai.


# Create your views here.
# after making serilaizers in views.py here we ill make api endpoints.


# genrics.ListCreateAPIView is a class based view which is used to display a list of all objects
# of a model and create a new object of a model.

# reverse ek function hai jo URL names se fully qualified URLs generate karne ke liye use hota hai.

@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        'rooms':reverse('room-list',request=request,format=format)
    })

# Class based views
class RoomList(generics.ListCreateAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer
    
    
class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer
    
# RetrieveUpdateDestroyAPIView is a class based view which is used to display a single object of a model
# and update and delete that object.




