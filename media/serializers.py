from rest_framework import serializers
from .models import Media

class MediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Media 
        fields = ('Title', 'Year', 'Rated', 'Released', 'Runtime', 'Genre', 'Director', 'Writer', 'Actors', 'Plot', 'Language', 'Country', 'Awards', 'Poster', 'Metascore', 'imdbRating', 'imdbVotes', 'imdbID', 'Type', 'DVD', 'BoxOffice', 'Production', 'Website')