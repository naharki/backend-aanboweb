from rest_framework import serializers
from ..models.models import Office

class OfficeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ["id", "office_name", "office_address", "office_slogan"]
