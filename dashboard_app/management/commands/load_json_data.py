# dashboard_app/management/commands/load_json_data.py

import json
from django.core.management.base import BaseCommand
from dashboard_app.models import DataPoint

class Command(BaseCommand):
    help = 'Load data from jsondata.json into DataPoint model'

    def handle(self, *args, **kwargs):
        with open('data/jsondata.json', 'r') as file:
            data = json.load(file)
            for item in data:

                DataPoint.objects.create(
                    end_year=item['end_year'],
                    intensity=item['intensity'],
                    sector=item['sector'],
                    topic=item['topic'],
                    insight=item['insight'],
                    url=item['url'],
                    region=item['region'],
                    start_year=item['start_year'],
                    impact=item['impact'],
                    added=item['added'],
                    published=item['published'],
                    country=item['country'],
                    relevance=item['relevance'],
                    pestle=item['pestle'],
                    source=item['source'],
                    title=item['title'],
                    likelihood=item['likelihood'],
                    
                )
        self.stdout.write(self.style.SUCCESS('Data successfully loaded'))
