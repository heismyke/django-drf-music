from django.contrib import admin
from app.models import Artist, Album, Song
# Register your models here.
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)