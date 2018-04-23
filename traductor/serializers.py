# -*- coding: utf-8 -*-
from rest_framework import serializers

class TextoSerializer(serializers.Serializer):
    """Your data serializer, define your fields here."""
    palabras = serializers.CharField()