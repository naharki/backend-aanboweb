from rest_framework import serializers
from ..models.leaders import Leader

class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = '__all__'
