from django.core.management.base import BaseCommand
from content.models import Track

class Command(BaseCommand):
    help = 'Seed database with sample podcast tracks'

    def handle(self, *args, **options):
        tracks_data = [
            {
                'title': 'The Future of Content Creation in Africa',
                'external_url': 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3',
                'order': 1,
            },
            {
                'title': 'Studio Secrets: Professional Lighting Tips',
                'external_url': 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3',
                'order': 2,
            },
            {
                'title': 'Interview with Ngandus Media Founder',
                'external_url': 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3',
                'order': 3,
            },
        ]

        for track_data in tracks_data:
            track, created = Track.objects.update_or_create(
                title=track_data['title'],
                defaults=track_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created track: {track.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Updated track: {track.title}'))

        self.stdout.write(self.style.SUCCESS(f'\nTotal tracks: {Track.objects.count()}'))
