from rest_framework import serializers
from django.db import models
from .models import Tag

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['name']