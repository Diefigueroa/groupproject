from django.db import models
import numpy as np


class squirrel(models.Model):
    objects = models.Manager()

    Latitude = models.FloatField(default=0)
    Longitude = models.FloatField(default=0)
    Unique_Squirrel_ID = models.CharField(max_length=200,primary_key=True)
    Shift = models.CharField(max_length=200)
    Date = models.DateField('date published')
    Age = models.CharField(max_length=200)
    Primary_Fur_Color = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    Specific_Location = models.CharField(max_length=200)
    Running = models.CharField(max_length=200)
    Chasing = models.CharField(max_length=200)
    Climbing = models.CharField(max_length=200)
    Eating = models.CharField(max_length=200)
    Foraging = models.CharField(max_length=200)
    Other_Activities = models.CharField(max_length=200)
    Kuks = models.CharField(max_length=200)
    Quaas = models.CharField(max_length=200)
    Moans = models.CharField(max_length=200)
    Tail_flags = models.CharField(max_length=200)
    Tail_twitches = models.CharField(max_length=200)
    Approaches = models.CharField(max_length=200)
    Indifferent = models.CharField(max_length=200)
    Runs_from = models.CharField(max_length=200)
    

    def __str__(self):
        return self.Unique_Squirrel_ID
    def get_absolute_url(self):
        return reverse('', kwargs={'id':self.Unique_Squirrel_ID})

# Create your models here.
