
from django.urls import path
from . import views


urlpatterns = [
    path('', views.music_list, name='music_list'),
    path('band/<int:band_id>/albums', views.albums, name='albums'),
    path('album/<int:album_id>/tracks', views.tracks, name='tracks'),
    path('stage/<int:stage_id>/band', views.stage_view, name='stage'),
]
