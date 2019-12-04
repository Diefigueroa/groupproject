from django.db import models
import numpy as np
from adaptor.model import CsvModel

class squirrel(CsvModel):
    Latitude = models.FloatField(default=0)
    Longitude = models.FloatField(default=0)
    Unique_Squirrel_ID = models.IntegerField(default=0)
    Shift = models.CharField(max_length=200)
    Date = models.DateField('date published')
    Age = models.CharField(max_length=200)
    Primary_Fur_Color = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    Specific_Location = models.CharField(max_length=200)
    Running = models.FloatField(default=0)
    Chasing = models.FloatField(default=0)
    Climbing = models.FloatField(default=0)
    Eating = models.FloatField(default=0)
    Foraging = models.FloatField(default=0)
    Other_Activities = models.CharField(max_length=200)
    Kuks = models.FloatField(default=0)
    Quaas = models.FloatField(default=0)
    Moans = models.FloatField(default=0)
    Tail_flags = models.FloatField(default=0)
    Tail_twitches = models.FloatField(default=0)
    Approaches = models.FloatField(default=0)
    Indifferent = models.FloatField(default=0)
    Runs_from = models.FloatField(default=0)

    def __str__(self):
        return self.Unique_squirrel_ID
    def get_absolute_url(self):
        return reverse('', kwargs={'id':self.Unique_squirrel_ID})

# Create your models here.
