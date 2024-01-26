from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=255, unique=True)
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Album(models.Model):
    name = models.CharField(max_length=255, unique=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    genre = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.name
    
class Song(models.Model):
    name = models.CharField(max_length=100, unique=True)
    minute = models.TimeField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs' )

    def __str__(self):
        return self.name