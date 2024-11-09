# products/models.py
from django.db import models

class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    Model_Description = models.CharField(max_length=100)
    Processor = models.CharField(max_length=50)
    RAM = models.CharField(max_length=20)
    Storage = models.CharField(max_length=50)
    Display = models.CharField(max_length=50)
    OS = models.CharField(max_length=50)
    Weight = models.CharField(max_length=20)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
