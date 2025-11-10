from django.db import models
from django.contrib.auth.models import User

class Office(models.Model):
    office_name = models.CharField(max_length=50)
    office_address = models.CharField(max_length=100)
    office_slogan = models.CharField(max_length=150)

    def __str__(self):
        return self.office_name
