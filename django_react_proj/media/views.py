from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Media
from .serializers import *

@api_view(['GET', 'POST'])
def medias_list(request):
    if request.method == 'GET':
        data = Media.objects.all()

        serializer = MediaSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)