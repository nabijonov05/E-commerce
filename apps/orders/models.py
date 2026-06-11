from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class Order(models.Model):

    status = models.CharField(max_length=20, default='pending')
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    address = models.TextField()

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.full_name