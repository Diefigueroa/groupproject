from django.db import models
from adaptor.model import CsvModel

class squirrel(CsvModel):
    Latitude = FloatField()
    Longitude = FloatField()
    Unique_Squirrel_ID = IntegerField()
    Shift = CharField()
    Date = DateField()
    Age = CharField()
    Primary_Fur_Color = CharField()
    Location = CharField()
    Specific_Location = CharField()
    Running = FloatField()
    Chasing = FloatField()
    Climbing = FloatField()
    Eating = FloatField()
    Foraging = FloatField()
    Other_Activities = CharField()
    Kuks = FloatField()
    Quaas = FloatField()
    Moans = FloatField()
    Tail_flags = FloatField()
    Tail_twitches = FloatField()
    Approaches = FloatField()
    Indifferent = FloatField()
    Runs_from = FloatField()

    class Meta:
        delimiter = ";"

# Create your models here.
