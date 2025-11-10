from django.shortcuts import render
from rest_framework import generics
from ..models.notice import Notice
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from ..serializers.notice_serializers import NoticeSerializer

# Create your views here.
class Notice_list (generics.ListAPIView):
    queryset = Notice.objects.all()
    serializer_class= NoticeSerializer
    permission_classes= [AllowAny]

class Notice_create (generics.CreateAPIView):
    queryset = Notice.objects.all()
    serializer_class= NoticeSerializer
    permission_classes= [IsAuthenticated]


class Notice_update_destroy (generics.RetrieveUpdateDestroyAPIView):
    queryset = Notice.objects.all()
    serializer_class= NoticeSerializer
    lookup_field= "pk"
    permission_classes =[IsAuthenticated]