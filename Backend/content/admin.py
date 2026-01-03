from django.contrib import admin
from .models import (
    SiteSettings, HeroSection, Event, AboutSection, 
    Service, ServiceVideo, Track, VideoGallery, 
    CountdownEvent, Testimonial, GalleryImage
)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'email', 'phone']
    fieldsets = (
        ('Branding', {'fields': ('site_name', 'tagline', 'logo')}),
        ('Contact Info', {'fields': ('phone', 'email')}),
        ('Social Media', {'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'youtube_url')}),
    )


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'is_active']
    list_filter = ['is_active']
    list_editable = ['is_active']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'location', 'is_active', 'order']
    list_filter = ['is_active', 'date']
    list_editable = ['is_active', 'order']
    search_fields = ['title', 'location']
    date_hierarchy = 'date'


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'price_description', 'is_featured', 'order']
    list_filter = ['is_featured']
    list_editable = ['is_featured', 'order']
    search_fields = ['title']


@admin.register(ServiceVideo)
class ServiceVideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_url', 'is_active']
    list_editable = ['is_active']


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_editable = ['order', 'is_active']


@admin.register(VideoGallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_url', 'is_active', 'order']
    list_filter = ['is_active']
    list_editable = ['is_active', 'order']
    search_fields = ['title']


@admin.register(CountdownEvent)
class CountdownEventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_date', 'is_active']
    list_filter = ['is_active']
    list_editable = ['is_active']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_title', 'is_active', 'order']
    list_filter = ['is_active']
    list_editable = ['is_active', 'order']


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_active', 'order']
    list_filter = ['is_active', 'category']
    list_editable = ['is_active', 'order']
    search_fields = ['title', 'category']
