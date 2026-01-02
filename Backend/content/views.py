from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    SiteSettings, HeroSection, Event, AboutSection,
    Service, ServiceVideo, Track, VideoGallery,
    CountdownEvent, Testimonial, GalleryImage
)
from .serializers import (
    SiteSettingsSerializer, HeroSectionSerializer, EventSerializer,
    AboutSectionSerializer, ServiceSerializer, ServiceVideoSerializer,
    TrackSerializer, VideoGallerySerializer, CountdownEventSerializer,
    TestimonialSerializer, GalleryImageSerializer
)


@api_view(['GET'])
def get_site_settings(request):
    """Get site settings (first entry)"""
    settings = SiteSettings.objects.first()
    if settings:
        serializer = SiteSettingsSerializer(settings)
        return Response(serializer.data)
    return Response({})


@api_view(['GET'])
def get_hero(request):
    """Get active hero section"""
    hero = HeroSection.objects.filter(is_active=True).first()
    if hero:
        serializer = HeroSectionSerializer(hero)
        return Response(serializer.data)
    return Response({})


@api_view(['GET'])
def get_events(request):
    """Get all active events"""
    events = Event.objects.filter(is_active=True)
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_about(request):
    """Get about section"""
    about = AboutSection.objects.first()
    if about:
        serializer = AboutSectionSerializer(about)
        return Response(serializer.data)
    return Response({})


@api_view(['GET'])
def get_services(request):
    """Get all services"""
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_service_video(request):
    """Get active service video"""
    video = ServiceVideo.objects.filter(is_active=True).first()
    if video:
        serializer = ServiceVideoSerializer(video)
        return Response(serializer.data)
    return Response({})


@api_view(['GET'])
def get_tracks(request):
    """Get all active tracks"""
    tracks = Track.objects.filter(is_active=True)
    serializer = TrackSerializer(tracks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_videos(request):
    """Get all active videos"""
    videos = VideoGallery.objects.filter(is_active=True)
    serializer = VideoGallerySerializer(videos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_countdown(request):
    """Get active countdown event"""
    countdown = CountdownEvent.objects.filter(is_active=True).first()
    if countdown:
        serializer = CountdownEventSerializer(countdown)
        return Response(serializer.data)
    return Response({})


@api_view(['GET'])
def get_testimonials(request):
    """Get all active testimonials"""
    testimonials = Testimonial.objects.filter(is_active=True)
    serializer = TestimonialSerializer(testimonials, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_gallery(request):
    """Get all active gallery images"""
    images = GalleryImage.objects.filter(is_active=True)
    serializer = GalleryImageSerializer(images, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_content(request):
    """Get all site content in one request"""
    data = {
        'settings': SiteSettingsSerializer(SiteSettings.objects.first()).data if SiteSettings.objects.exists() else {},
        'hero': HeroSectionSerializer(HeroSection.objects.filter(is_active=True).first()).data if HeroSection.objects.filter(is_active=True).exists() else {},
        'events': EventSerializer(Event.objects.filter(is_active=True), many=True).data,
        'about': AboutSectionSerializer(AboutSection.objects.first()).data if AboutSection.objects.exists() else {},
        'services': ServiceSerializer(Service.objects.all(), many=True).data,
        'service_video': ServiceVideoSerializer(ServiceVideo.objects.filter(is_active=True).first()).data if ServiceVideo.objects.filter(is_active=True).exists() else {},
        'tracks': TrackSerializer(Track.objects.filter(is_active=True), many=True).data,
        'videos': VideoGallerySerializer(VideoGallery.objects.filter(is_active=True), many=True).data,
        'countdown': CountdownEventSerializer(CountdownEvent.objects.filter(is_active=True).first()).data if CountdownEvent.objects.filter(is_active=True).exists() else {},
        'testimonials': TestimonialSerializer(Testimonial.objects.filter(is_active=True), many=True).data,
        'gallery': GalleryImageSerializer(GalleryImage.objects.filter(is_active=True), many=True).data,
    }
    return Response(data)
