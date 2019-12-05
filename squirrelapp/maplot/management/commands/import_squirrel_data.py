from django.core.management.base import BaseCommand, CommandError
from maplot.models import squirrel
import pandas as pd
import os
import re, sys,request,csv
from datetime import date
class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
        # Positional arguments
    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        path = options['path']
        pattern = re.compile(r'(\d{2})(\d{2})(\d{4})')

        with open(path) as f:
            data = csv.DictReader(f)
            for row in data :
                i,j,k = pattern.match(row.get('date')).groups()
                obj, created = squirrel.objects.get_or_create(
                    Latitude = row.get('y'),
                    Longitude = row.get('x'),
                    Unique_squirrel_ID = row.get('unique_squirrel_id'),
                    Hectare = row.get('hectare'),
                    Shift = row.get('shift'),
                    Date = date(int(k),int(i),int(j)),
                    Hectare_squirrel_num = row.get('hectare_squirrel_number'),
                    Age = row.get('age'),
                    Primary_fur_color = row.get('primary_fur_color'),
                    Location = row.get('location'),
                    Specific_location = row.get('specific_location'),
                    Chasing = row.get('chasing'),
                    Running = row.get('running'),
                    Climbing = row.get('climbing'),
                    Eating = row.get('eating'),
                    Foraging = row.get('foraging'),
                    Other_Activities = row.get('other_activities'),
                    Kuks = row.get('kuks'),
                    Quaas = row.get('quaas'),
                    Moans = row.get('moans'),
                    Tail_Flags = row.get('tail_flags'),
                    Tail_Twitches = row.get('tail_twitches'),
                    Approaches = row.get('approaches'),
                    Indifferent = row.get('indifferent'),
                    Runs_From = row.get('runs_from'),
    )
        self.stdout.write(self.style.SUCCESS(f'Successfully import squirrel data from {path}'))


