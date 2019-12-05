from django.core.management.base import BaseCommand
from maplot.models import squirrel
import requests, csv, re, sys
from dateutil import parser
from datetime import date

class Command(BaseCommand):
    help ='Export squirrel data from NYC Central Park'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='path of file to be exported')

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        
        with open(path, mode='wb') as csvfile:
            writer = csv.writer(csvfile)
            squirrels = squirrel.objects.all()
            writer.writerow['X','Y','Unique Squirrel ID',
                    'Shift','Date','Age','Primary Fur Color','Location','Specific Location','Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from']

                        

            for squirrel in squirrels:
                    writer.writerow([
                    squirrel.Latitude,Longitude,
                    squirrel.Unique_Squirrel_ID,
                    squirrel.Shift,
                    squirrel.Date ,
                    squirrel.Age ,
                    squirrel.Primary_Fur_Color ,
                    squirrel.Location ,
                    squirrel.Specific_Location ,
                    squirrel.Running ,
                    squirrel.Chasing ,
                    squirrel.Climbing ,
                    squirrel.Eating ,
                    squirrel.Foraging ,
                    squirrel.Other_Activities ,
                    squirrel.Kuks ,
                    squirrel.Quaas ,
                    squirrel.Moans ,
                    squirrel.Tail_Flags ,
                    squirrel.Tail_Twitches ,
                    squirrel.Approaches ,
                    squirrel.Indifferent ,
                    squirrel.Runs_From ,
                ])
        csvfile.close() 
        

