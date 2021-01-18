from django.db import models


class Band(models.Model):
    band_name = models.CharField('Название группы', max_length=50)

    def __str__(self):
        return self.band_name


class Album(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    name = models.CharField('Название альбома', max_length=50)
    picture = models.URLField('Обложка альбома')
    release_date = models.DateField('Дата выхода альбома', max_length=50)

    def __str__(self):
        return self.name


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_name = models.CharField('Название песни', max_length=50)
    play_time = models.IntegerField('Длительность песни', blank=True, null=True)

    def __str__(self):
        return self.song_name


class Stages(models.Model):
    stage_name = models.CharField('Название площадки', max_length=50)
    band_mtm = models.ManyToManyField(Band)

    def __str__(self):
        return self.stage_name