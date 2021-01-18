from django.contrib import admin

from .models import Album, Band, Track, Stages

admin.site.register(Album)
admin.site.register(Band)
admin.site.register(Track)
admin.site.register(Stages)
