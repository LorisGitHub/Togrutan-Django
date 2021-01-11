from rest_framework import serializers
from .models import User
from django import forms

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('Username', 'Viewed', 'PlanToWatch', 'Dropped')