# Basically serilizers are used to convert complex data types such as 
# querysets and model instances to native Python data types that can 
# then be easily rendered into JSON, XML or other content types.

#matlab jab humen apne python backend se kisi model ka data kisi dosre front end mn kisi 
# kisi dosre data type mn bhejna hota like json then we use serlializers.

from rest_framework import serializers

from .models import Room,RoomImage
# Django REST Framework me HyperlinkedModelSerializer ka maqsad data ko IDs ki jagah 
# hyperlinks ke zariye represent karna hai.
# fields ka matlab hai ke humen kon kon se fields ko serilize karna hai.
# serializers is used to convert the modle instance in another format like json.




class RoomImageSeializer(serializers.ModelSerializer):
    room=serializers.HyperlinkedRelatedField(view_name="room-detail",queryset=Room.objects.all()),
    class Meta:
        model=RoomImage
        fields=['id','image','caption','room']

# HyperlinkedRelatedField is used to represent the related field as a hyperlink.
# view_name is used to specify the name of the view.
# queryset is used to specify the queryset for the related field.
# fields is used to specify the fields to be serialized.
#Meta class is used to specify the model and fields to be serialized.



class RoomSerializer(serializers.HyperlinkedModelSerializer):
    images=RoomImageSeializer(many=True,read_only=True)
    
    
    # many=True is used to serialize multiple objects.
    # read_only=True is used to make the field read-only.
    class Meta:
        model=Room
        fields=["url","id","name","type","pricePerNight","currency","maxOccupancy","description",'images']
