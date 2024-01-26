from django.urls import path
from app.api.views import (get_artists, 
                           artist_details,
                           get_album,
                           album_details,
                           get_songs,
                            song_details
                           )
                        


urlpatterns = [
    path('artists/', get_artists.as_view(), name='Artists' ),
    path('artists/<int:pk>', artist_details.as_view(), name='Artists-Details' ),

    path('artists/<int:pk>/albums/', get_album.as_view(), name='Album'),
    path('artists/<int:pk>/albums/<int:album_pk>', get_album.as_view(), name='Album'),

     path('albums/', get_album.as_view(), name='Album-Details'),
    path('albums/<int:pk>', album_details.as_view(), name='Album-Details'),

    path('artists/<int:pk>/albums/songs/', get_songs.as_view(), name='Songs'),
   

    path('albums/<int:pk>/songs/', get_songs.as_view(), name='Songs'),
    path('albums/<int:pk>/songs/<int:song_pk>/', song_details.as_view(), name='Songs-details'),
]
