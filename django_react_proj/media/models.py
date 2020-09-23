from django.db import models

class Media(models.Model):
    Title = models.CharField(max_length=50)
    Year = models.IntegerField()
    Rated = models.CharField(max_length=50)
    Released = models.DateField()
    Runtime = models.CharField(max_length=50)
    Genre = models.CharField(max_length=50)
    Director = models.CharField(max_length=50)
    Writer = models.CharField(max_length=200)
    Actors = models.CharField(max_length=100)
    Plot = models.CharField(max_length=250)
    Language = models.CharField(max_length=100)
    Country = models.CharField(max_length=50)
    Awards = models.CharField(max_length=100)
    Poster = models.URLField()
    Metascore = models.FloatField()
    imdbRating = models.FloatField()
    imdbVotes = models.FloatField()
    imdbID = models.CharField(max_length=50)
    Type = models.CharField(max_length=50)
    DVD = models.DateField()
    BoxOffice = models.CharField(max_length=50)
    Production = models.CharField(max_length=50)
    Website = models.CharField(max_length=50)

    def __str__(self):
        return self.Title