from django.db import models
from datetime import datetime

# Create your models here.

class ContactUs(models.Model):
    full_name = models.CharField(max_length= 150)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    subject = models.TextField(blank=True)
    company = models.CharField(max_length=100) 
    message = models.TextField(blank=True)
    created_one = models.DateTimeField(blank=True,default= datetime.now)

    def __str__(self) -> str:
        return self.full_name 
