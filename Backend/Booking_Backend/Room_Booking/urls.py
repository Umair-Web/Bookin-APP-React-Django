from django.urls import path
from Room_Booking import views
from rest_framework.urlpatterns import format_suffix_patterns
# fomrant_suffix_patterns is used to add suffixes to the urls like .json or .api etc.
# basically it is used to add suffixes to the urls.

urlpatterns = [
    path('',views.api_root,name="api_root"),
    path("rooms/",views.RoomList.as_view(),name="room-list"),
    path("rooms/<int:pk>/",views.RoomDetail.as_view(),name="room-detail"),
    path("occupied-dates/",views.OccupiedDatesList.as_view(),name="occupieddate-list"),
    path("occupied-dates/<int:pk>/",views.OccupiedDatesDetails.as_view(),name="occupieddate-detail"),
]

urlpatterns=format_suffix_patterns(urlpatterns)
# Yeh allow karta hai ke hum API URLs ke saath format suffix laga sakein, jaise /rooms.json ya /rooms.xml

from django.conf import settings
from django.conf.urls.static import static
# Settings aur static ko import kar raha hai jo media files serve karne ke liye zaroori hai.

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
#Agar DEBUG=True hai (development mode me hain), to media files (/media/) serve hongi.
#Ye static files ko local development ke dauraan serve karne me madad karta hai.
# Basically it is used to get image offline with the help of url