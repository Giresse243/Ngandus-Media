from django.core.management.base import BaseCommand
from content.models import Service


class Command(BaseCommand):
    help = 'Seed database with Ngandus Media services'

    def handle(self, *args, **options):
        services_data = [
            {
                'title': 'Video Production',
                'description': 'Professional video production for YouTube channels, documentaries, and promotional content.',
                'price': 2500.00,
                'price_description': 'From',
                'is_featured': True,
                'order': 1,
            },
            {
                'title': 'Photography',
                'description': 'Studio photography, professional portraits, product shoots, and creative headshots.',
                'price': 1800.00,
                'price_description': 'From',
                'is_featured': True,
                'order': 2,
            },
            {
                'title': 'Wedding Coverage',
                'description': 'Capture your special day with full-day photography and videography services.',
                'price': 8500.00,
                'price_description': 'From',
                'is_featured': True,
                'order': 3,
            },
            {
                'title': 'Event Coverage',
                'description': 'Professional coverage for corporate events, parties, clubs, and cultural manifestations.',
                'price': 3500.00,
                'price_description': 'From',
                'is_featured': True,
                'order': 4,
            },
            {
                'title': 'Podcast & Emissions',
                'description': 'Professional audio and video recording for podcasts and broadcast shows.',
                'price': 1200.00,
                'price_description': 'Per hour',
                'is_featured': True,
                'order': 5,
            },
            {
                'title': 'Film Production',
                'description': 'Creative short films, music videos, and high-quality cinematic productions.',
                'price': 15000.00,
                'price_description': 'From',
                'is_featured': True,
                'order': 6,
            },
        ]

        for service_data in services_data:
            service, created = Service.objects.update_or_create(
                title=service_data['title'],
                defaults=service_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created: {service.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Updated: {service.title}'))

        self.stdout.write(self.style.SUCCESS(f'\nTotal services: {Service.objects.count()}'))
