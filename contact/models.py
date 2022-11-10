from django.db import models

# Create your models here.
class Customer(models.Model):
    full_name = models.CharField(null=True,max_length=100)
    email = models.EmailField(null=True,max_length=100)
    subject = models.CharField(null=True,max_length=100)
    message = models.CharField(max_length=100)
