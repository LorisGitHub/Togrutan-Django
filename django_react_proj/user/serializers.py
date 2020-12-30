from rest_framework import serializers
from .models import User
from django import forms

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        widget = {
            'Password': forms.PasswordInput(),
        }
        fields = ('Username', 'Password', 'Viewed', 'PlanToWatch', 'Dropped')