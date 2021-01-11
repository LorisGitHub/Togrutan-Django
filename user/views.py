from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
from .models import User
from .serializers import *

@api_view(['GET', 'POST'])
def users_list(request):
    if request.method == 'GET':
        data = User.objects.all()

        serializer = UserSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)


@api_view(['GET', 'POST'])
def user_info(request):
    if request.method == 'GET':
        data = User.objects.filter(Username=request.query_params.get("username"))
        return JsonResponse(list(data.values())[0], safe=False)
    if request.method == 'POST':
        user = json.loads(request.data.get("user"))
        print(user)
        dbUser = User.objects.filter(Username=user["username"])

        if user["viewed"] and len(user["viewed"])>0:
            splitView = ";".join(user["viewed"])
            dbUser.update(Viewed=splitView)

        if user["planToWatch"] and len(user["planToWatch"])>0:
            splitPlan = ";".join(user["planToWatch"])
            dbUser.update(PlanToWatch=splitPlan)

        if user["dropped"] and len(user["dropped"])>0:
            splitDrop = ";".join(user["dropped"])
            dbUser.update(Dropped=splitDrop)
        
        return Response("Updated")