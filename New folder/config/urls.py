from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Customize admin site
admin.site.site_header = "Ngandus Media Admin"
admin.site.site_title = "Ngandus Media"
admin.site.index_title = "Content Management"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/content/', include('content.urls')),
    path('api/bookings/', include('bookings.urls')),
    path('api/contact/', include('contact.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
