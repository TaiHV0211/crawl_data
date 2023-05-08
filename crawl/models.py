from django.db import models
from django.db.models import QuerySet

# Create your models here.

MAX_LENGTH = 10000


class RealEstate(models.Model):
    #   'address' : address,
    #   'bedrooms' : bedrooms,
    #   'bathrooms' : bathrooms,
    #   'agent_name': agent_name,
    #   'aria_code' : aria_code,
    #   'telephones' : telephones,
    #   'prices' : prices

    address = models.CharField(max_length=255)
    bedrooms = models.CharField(max_length=255)
    bathrooms = models.CharField(max_length=255)
    agent_name = models.CharField(max_length=255)
    aria_code = models.CharField(max_length=255)
    telephones = models.CharField(max_length=255)
    prices = models.FloatField()
    highrespath = models.CharField(max_length=MAX_LENGTH)
    medrespath = models.CharField(max_length=MAX_LENGTH)
    lowrespath = models.CharField(max_length=MAX_LENGTH)
    descriptions = models.CharField(max_length=MAX_LENGTH, blank=True, null=True)


    class Meta:
        db_table = 'real_estate'
