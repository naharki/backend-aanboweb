from django.shortcuts import render
from rest_framework import generics
from ..models.leaders import Leader
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from ..serializers.leader_serializers import LeaderSerializer

# Create your views here.
class Leader_list (generics.ListAPIView):
    queryset = Leader.objects.all()
    serializer_class= LeaderSerializer
    permission_classes= [AllowAny]

class Leader_create (generics.CreateAPIView):
    queryset = Leader.objects.all()
    serializer_class= LeaderSerializer
    permission_classes= [IsAuthenticated]


class Leader_update_destroy (generics.RetrieveUpdateDestroyAPIView):
    queryset = Leader.objects.all()
    serializer_class= LeaderSerializer
    lookup_field= "pk"
    permission_classes =[IsAuthenticated]