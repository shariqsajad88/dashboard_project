from django.db import models

# Create your models here.
from django.db import models

class DataPoint(models.Model):
    end_year = models.CharField(max_length=100)
    intensity = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    insight = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100)
    impact = models.CharField(max_length=100)
    added = models.CharField(max_length=100)
    published = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    relevance = models.CharField(max_length=100)
    pestle = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    
    title = models.CharField(max_length=100)
    likelihood = models.CharField(max_length=100)
    
