# Basically serilizers are used to convert complex data types such as 
# querysets and model instances to native Python data types that can 
# then be easily rendered into JSON, XML or other content types.

#matlab jab humen apne python backend se kisi model ka data kisi dore fornt end mn kisi 
# kisi dosre data type mn bhejna hota like json then we use serlializers.

from rest_framework import serializers

from .models import Room
# Django REST Framework me HyperlinkedModelSerializer ka maqsad data ko IDs ki jagah 
# hyperlinks ke zariye represent karna hai.
# fields ka matlab hai ke humen kon kon se fields ko serilize karna hai.

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Room
        fields=["url","id","name","type","pricePerNight","currency","maxOccupancy","description"]
