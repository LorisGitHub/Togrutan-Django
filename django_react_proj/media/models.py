from django.db import models

class Media(models.Model):
    Title = models.CharField(max_length=100, default='')
    Year = models.IntegerField()
    Rated = models.CharField(max_length=100, blank=True, default='')
    Released = models.DateField(blank=True)
    Runtime = models.CharField(max_length=100, blank=True, default='')
    Genre = models.CharField(max_length=100, blank=True, default='')
    Director = models.CharField(max_length=500, blank=True, default='')
    Writer = models.CharField(max_length=500, blank=True, default='')
    Actors = models.CharField(max_length=500, blank=True, default='')
    Plot = models.CharField(max_length=500, blank=True, default='')
    Language = models.CharField(max_length=100, blank=True, default='')
    Country = models.CharField(max_length=100, blank=True, default='')
    Awards = models.CharField(max_length=100, blank=True, default='')
    Poster = models.URLField()
    Metascore = models.FloatField(blank=True, null=True)
    imdbRating = models.FloatField(blank=True, null=True)
    imdbVotes = models.FloatField(blank=True, null=True)
    imdbID = models.CharField(max_length=100, default='')
    Type = models.CharField(max_length=100, default='')
    Seasons = models.IntegerField(blank=True, null=True)
    DVD = models.DateField(blank=True, null=True)
    BoxOffice = models.CharField(max_length=100, blank=True, default='')
    Production = models.CharField(max_length=100, blank=True, default='')
    Website = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.Title