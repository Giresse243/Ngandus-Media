from django.urls import path
from . import views

urlpatterns = [
    path('settings/', views.get_site_settings, name='site-settings'),
    path('hero/', views.get_hero, name='hero'),
    path('events/', views.get_events, name='events'),
    path('about/', views.get_about, name='about'),
    path('services/', views.get_services, name='services'),
    path('service-video/', views.get_service_video, name='service-video'),
    path('tracks/', views.get_tracks, name='tracks'),
    path('videos/', views.get_videos, name='videos'),
    path('countdown/', views.get_countdown, name='countdown'),
    path('testimonials/', views.get_testimonials, name='testimonials'),
    path('gallery/', views.get_gallery, name='gallery'),
    path('all/', views.get_all_content, name='all-content'),
]
