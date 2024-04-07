from django.db import models

# Create your models here.

class Hotels(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=200)
    price = models.IntegerField(null=False, default=0)
    availability = models.BooleanField(default=True)