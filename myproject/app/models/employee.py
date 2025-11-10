from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    employee_name = models.CharField(max_length=50)
    employee_address = models.CharField(max_length=100)
    employee_contact = models.CharField(max_length=150)
    employee_position = models.CharField(max_length=150)
    employee_section = models.CharField(max_length=150)
    employee_email = models.CharField(max_length=150)

    def __str__(self):
        return self.employee_name
