from rest_framework import serializers, viewsets
from .models import dht
class Dhtserializer(serializers.ModelSerializer):
    class Meta :
        model = dht
        fields = ['id', 'temp','dt']