from django.core.management.base import BaseCommand
from content.models import Event
from datetime import date


class Command(BaseCommand):
    help = 'Seed database with sample events/projects'

    def handle(self, *args, **options):
        events_data = [
            {
                'title': 'Wedding Coverage - Johannesburg',
                'category': 'Wedding',
                'description': 'Full Day Photography & Video',
                'date': date(2024, 6, 15),
                'location': 'Johannesburg, South Africa',
                'order': 1,
            },
            {
                'title': 'Music Video Production',
                'category': 'Music Video',
                'description': 'Professional Music Video Shoot',
                'date': date(2024, 5, 20),
                'location': 'Pretoria, South Africa',
                'order': 2,
            },
            {
                'title': 'Corporate Event Coverage',
                'category': 'Event',
                'description': 'Business Conference & Gala',
                'date': date(2024, 4, 10),
                'location': 'Cape Town, South Africa',
                'order': 3,
            },
            {
                'title': 'YouTube Content Creation',
                'category': 'YouTube',
                'description': 'Channel Production & Editing',
                'date': date(2024, 3, 5),
                'location': 'Durban, South Africa',
                'order': 4,
            },
        ]

        for event_data in events_data:
            event, created = Event.objects.update_or_create(
                title=event_data['title'],
                defaults=event_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created: {event.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Updated: {event.title}'))

        self.stdout.write(self.style.SUCCESS(f'\nTotal events: {Event.objects.count()}'))
