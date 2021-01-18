from django.shortcuts import render
from .models import Album, Band, Track, Stages


def music_list(request):
    bands = Band.objects.all()
    stage = Stages.objects.all()
    return render(request, 'music/music_list.html', {'bands': bands, 'stage': stage})


def albums(request, band_id):
    band = Band.objects.get(id=band_id)
    albums = Album.objects.filter(band=band_id)
    stages = band.stages_set.all()
    return render(request, 'music/albums.html', {'albums': albums, 'band': band, 'stages': stages})


def tracks(request, album_id):
    album = Album.objects.get(id=album_id)
    tracks = Track.objects.filter(album=album_id)
    return render(request, 'music/tracks.html', {'album': album, 'tracks': tracks})


def stage_view(request, stage_id):
    band = Stages.objects.get(id=stage_id).band_mtm.all()
    return render(request, 'music/stages.html', {'band': band})



