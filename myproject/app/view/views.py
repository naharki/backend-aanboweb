from django.shortcuts import render
from rest_framework import generics
from ..models.models import Office
from ..serializers.serializers import OfficeSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser

# Create your views here.
class Office_profile_list (generics.ListAPIView):
    queryset = Office.objects.all()
    serializer_class= OfficeSerializer
    permission_classes= [AllowAny]

class Office_profile_create (generics.CreateAPIView):
    queryset = Office.objects.all()
    serializer_class= OfficeSerializer
    permission_classes= [IsAuthenticated]


class Office_profile_update_destroy (generics.RetrieveUpdateDestroyAPIView):
    queryset = Office.objects.all()
    serializer_class= OfficeSerializer
    lookup_field= "pk"
    permission_classes =[IsAuthenticated]