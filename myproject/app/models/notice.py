from django.db import models
from django.contrib.auth.models import User

class Notice(models.Model):
    notice_title= models.CharField(max_length=150)
    notice_content = models.TextField()
    notice_published_date = models.DateField(auto_now_add=True, blank=True, null=True)
    notice_file = models.FileField(null=True, blank=True, upload_to='notices/')

    def __str__(self):
        return self.notice_title
