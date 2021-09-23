from django.db import models

class Loja(models.Model):
    address = models.CharField(max_length=95, blank=True)
    categories = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=189, blank=True)
    country = models.CharField(max_length=56, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True)
    name = models.CharField(max_length=200, blank=True)
    postalCode = models.CharField(max_length=20, blank=True)
    province = models.CharField(max_length=2, blank=True)
    websites = models.CharField(max_length=2083, blank=True)