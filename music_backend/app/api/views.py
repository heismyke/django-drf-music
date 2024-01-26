from rest_framework.views import APIView
from rest_framework import generics,mixins
from app.models import Artist, Album, Song
from app.api.serializers import ArtistSerializer, AlbumSerializer, SongSerializer
from rest_framework.response import Response
from rest_framework import status

class get_artists(APIView):
    def get(self, request):
        qs = Artist.objects.all()
        serializer = ArtistSerializer(qs, many=True)
        return Response(serializer.data)
    def post (self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
class artist_details(APIView):
    def get(self, request, pk):
        try:
            qs = Artist.objects.get(pk=pk)
            serializer = ArtistSerializer(qs)
            return Response(serializer.data)
        except Artist.DoesNotExist:
            return Response({'error': 'Artist not found'}, status=status.HTTP_404_NOT_FOUND)
    def put(self, request, pk):
            qs = Artist.objects.get(pk=pk)
            serializer = ArtistSerializer(qs, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        qs = Artist.objects.get(pk=pk)
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class get_album(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get(self, request, *arg, **kwargs):
        return self.list(request, *arg, **kwargs)

    def post(self, request, *arg, **kwargs):
        return self.create(request, *arg, **kwargs)



class album_details(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView,):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get(self, request, album_pk, *arg, **kwargs):
        return self.retrieve(request, album_pk, *arg, **kwargs)
    
    def put(self, request, *arg, **kwargs):
        print("Additional positional arguments (*args):", arg)
        print("Additional keyword arguments (**kwargs):", kwargs)
        return self.update(request, *arg, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
class get_songs(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get(self, request, *arg, **kwargs):
        return self.list(request, *arg, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    

class song_details(APIView):
    def get(self, request, song_pk, **kwargs):
        try:
            qs = Song.objects.get(pk=song_pk)
            serializer = SongSerializer(qs)
            return Response(serializer.data)
        except Song.DoesNotExist:
            return Response({'error': 'song not found'}, status=status.HTTP_404_NOT_FOUND)
    def put(self, request, song_pk):
            qs = Song.objects.get(pk=song_pk)
            serializer = SongSerializer(qs, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, song_pk):
        qs = Song.objects.get(pk=song_pk)
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
      