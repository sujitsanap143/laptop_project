from django.db import models

# Create your models here.

class Laptops(models.Model):
    laptop_id = models.IntegerField(unique=True)
    model_name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    ram = models.IntegerField()
    processor = models.CharField(max_length=20)
    price = models.FloatField()
