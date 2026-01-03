from django.db import models


class SiteSettings(models.Model):
    """General site settings"""
    site_name = models.CharField(max_length=100, default="Ngandus Media")
    tagline = models.CharField(max_length=200, blank=True)
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
    
    def __str__(self):
        return self.site_name


class HeroSection(models.Model):
    """Hero banner section"""
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    background_image = models.ImageField(upload_to='hero/')
    video_url = models.URLField(blank=True, help_text="YouTube video URL")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Sections"
    
    def __str__(self):
        return self.title


class Event(models.Model):
    """Events/Projects section"""
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order', '-date']
        verbose_name = "Event/Project"
        verbose_name_plural = "Events/Projects"
    
    def __str__(self):
        return self.title


class AboutSection(models.Model):
    """About section content"""
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')
    button_text = models.CharField(max_length=50, default="Contact Us")
    button_url = models.CharField(max_length=200, default="#contact")
    
    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Sections"
    
    def __str__(self):
        return self.title


class Service(models.Model):
    """Studio services"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='services/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Starting price in ZAR")
    price_description = models.CharField(max_length=200, blank=True, help_text="e.g., 'Starting from' or 'Per hour'")
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title


class ServiceVideo(models.Model):
    """Video for services section"""
    title = models.CharField(max_length=200, blank=True)
    video_url = models.URLField(help_text="YouTube video URL")
    thumbnail = models.ImageField(upload_to='services/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Service Video"
        verbose_name_plural = "Service Videos"
    
    def __str__(self):
        return self.title or "Service Video"


class Track(models.Model):
    """Music/Audio tracks (if applicable)"""
    title = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='tracks/', blank=True, null=True)
    external_url = models.URLField(blank=True, help_text="Or link to external audio")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title


class VideoGallery(models.Model):
    """YouTube/Video gallery items"""
    title = models.CharField(max_length=200)
    video_url = models.URLField(help_text="YouTube video URL")
    thumbnail = models.ImageField(upload_to='videos/')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Video"
        verbose_name_plural = "Video Gallery"
    
    def __str__(self):
        return self.title


class CountdownEvent(models.Model):
    """Featured countdown event"""
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    event_date = models.DateTimeField()
    background_image = models.ImageField(upload_to='countdown/')
    button_text = models.CharField(max_length=50, default="Book Now")
    button_url = models.CharField(max_length=200, default="#booking")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Countdown Event"
        verbose_name_plural = "Countdown Events"
    
    def __str__(self):
        return self.title


class Testimonial(models.Model):
    """Client testimonials"""
    client_name = models.CharField(max_length=100)
    client_title = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.client_name


class GalleryImage(models.Model):
    """Image gallery/Portfolio"""
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"
    
    def __str__(self):
        return self.title or f"Image {self.pk}"
