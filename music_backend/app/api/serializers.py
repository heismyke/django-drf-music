from rest_framework import serializers
from app.models import Artist, Album, Song

class SongSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Song
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)
    class Meta:
        model = Album
        fields = ['id','name', 'genre', 'date', 'songs']

class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True)
    class Meta:
        model = Artist
        fields = ['name', 'albums']



