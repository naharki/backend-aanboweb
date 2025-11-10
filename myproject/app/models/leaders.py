from django.db import models
from django.contrib.auth.models import User

class Leader(models.Model):
    leader_name = models.CharField(max_length=50)
    leader_contact = models.CharField(max_length=150)
    leader_position = models.CharField(max_length=150)
    leader_email = models.EmailField(max_length=150)
    leader_photo = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.leader_name
