from django.core.management.base import BaseCommand, CommandError

from maplot.models import squirrel
import pandas as pd
import os
import re, sys, csv
from datetime import date

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

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
                    Unique_Squirrel_ID = row.get('unique_squirrel_id'),
                    Shift = row.get('shift'),
                    Date = date(int(k),int(i),int(j)),
                    Age = row.get('age'),
                    Primary_Fur_Color = row.get('primary_fur_color'),
                    Location = row.get('location'),
                    Specific_Location = row.get('specific_location'),
                    Chasing = row.get('chasing'),
                    Running = row.get('running'),
                    Climbing = row.get('climbing'),
                    Eating = row.get('eating'),
                    Foraging = row.get('foraging'),
                    Other_Activities = row.get('other_activities'),
                    Kuks = row.get('kuks'),
                    Quaas = row.get('quaas'),
                    Moans = row.get('moans'),
                    Tail_flags = row.get('tail_flags'),
                    Tail_twitches = row.get('tail_twitches'),
                    Approaches = row.get('approaches'),
                    Indifferent = row.get('indifferent'),
                    Runs_from = row.get('runs_from'),
    )
        self.stdout.write(self.style.SUCCESS(f'Successfully import squirrel data from {path}'))

