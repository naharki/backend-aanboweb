from django.shortcuts import render
from rest_framework import generics
from ..models.employee import Employee
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from ..serializers.employee_serializers import EmployeeSerializer

# Create your views here.
class Employee_list (generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class= EmployeeSerializer
    permission_classes= [AllowAny]

class Employee_create (generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class= EmployeeSerializer
    permission_classes= [IsAuthenticated]


class Employee_update_destroy (generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class= EmployeeSerializer
    lookup_field= "pk"
    permission_classes =[IsAuthenticated]