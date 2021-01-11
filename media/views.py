from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from .models import Media
from .IMDb import *
from .serializers import *

@api_view(['GET', 'POST'])
def medias_list(request):
    if request.method == 'GET':
        data = Media.objects.all()

        serializer = MediaSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

@api_view()
@permission_classes([AllowAny])
def medias_preview(request):
    if request.method == 'GET':
        db = IMDb()
        
        print("Looking for: " + request.query_params.get("data"))
        research = db.search(request.query_params.get("data"),limit=6) # recherche les films Aveng dans imdb 
        # si recherche illimité, retire limit=
        previews = []
        for k in research:
            previews.append(k.__dict__)

        return Response(previews)

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def getMediaFromImdbID(request):
    if request.method == 'GET':
        
        db = IMDb()
        movieId = request.query_params.get("imdbId")

        result = db.infoMovie(movieId)

        return Response(result.__dict__ if result != None else None)

    elif request.method == 'POST':
        db = IMDb()
        
        print("Looking for: " + request.query_params.get("id"))

        result = db.infoMovie(request.query_params.get("id")) # Avengers endgame

        if(result != None):
            print(result.__dict__)
            media = Media()
            media.Title = result.title
            media.Year = int(result.year)
            media.Rated = result.contentRating
            media.Released = result.released
            media.Runtime = result.duration
            media.Genre = " , ".join(result.genre)
            media.Director = " , ".join(result.directors)
            media.Writer = " , ".join(result.creators)
            media.Actors = " , ".join(result.actors)
            media.Plot = result.plot
            media.Language = ""
            media.Country = ""
            media.Awards = ""
            media.Poster = result.image
            media.Metascore = result.metascore if result.metascore != "N/A" else None
            media.imdbRating = result.imdbRating if result.imdbRating != "N/A" else None
            media.imdbVotes = result.imdbVotes if result.imdbVotes != "N/A" else None
            media.imdbID = result.imdbID
            media.Type = result.type
            # media.Seasons = result.seasons if result.contentRating
            # media.DVD = result.contentRating
            # media.BoxOffice = result.contentRating
            # media.Production = result.contentRating
            # media.Website = result.contentRating
            media.save()

        return Response(result.__dict__ if result != None else None)


@api_view(['POST'])
def getMultipleMediaFromImdbID(request):
    if request.method == 'POST':
        
        db = IMDb()
        ids = request.data.get("ids")
        listMovies = []

        for movieId in ids:
            result = db.infoMovie(movieId)
            if(result != None):
                listMovies.append(result.__dict__)

        return Response(listMovies if listMovies != None and len(listMovies)>0 else None)