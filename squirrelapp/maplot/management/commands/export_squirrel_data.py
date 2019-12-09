from django.core.management.base import BaseCommand
from maplot.models import squirrel
import csv, re, sys
from dateutil import parser
from datetime import date

class Command(BaseCommand):
    help ='Export squirrel data from NYC Central Park'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='path of file to be exported')

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, mode='w') as csvfile:
            writer = csv.writer(csvfile)
            squirrels = squirrel.objects.all()
            writer.writerow(['X','Y','Unique Squirrel ID','Shift','Date','Age','Primary Fur Color','Location','Specific Location','Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from'])

                        

            for row in squirrels:
                    writer.writerow([
                    row.latitude,row.longitude,
                    row.Unique_Squirrel_ID,
                    row.Shift,
                    row.Date ,
                    row.Age ,
                    row.Primary_Fur_Color ,
                    row.Location ,
                    row.Specific_Location ,
                    row.Running ,
                    row.Chasing ,
                    row.Climbing ,
                    row.Eating ,
                    row.Foraging ,
                    row.Other_Activities ,
                    row.Kuks ,
                    row.Quaas ,
                    row.Moans ,
                    row.Tail_flags ,
                    row.Tail_twitches ,
                    row.Approaches ,
                    row.Indifferent ,
                    row.Runs_from ,
                ])
        csvfile.close() 
        

