from django.contrib import admin
from .models import BookingRequest


@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'service', 'preferred_date', 'status', 'created_at']
    list_filter = ['status', 'service', 'preferred_date', 'created_at']
    list_editable = ['status']
    search_fields = ['name', 'email', 'service']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Client Information', {'fields': ('name', 'email', 'phone')}),
        ('Booking Details', {'fields': ('service', 'preferred_date', 'preferred_time', 'message')}),
        ('Status', {'fields': ('status',)}),
        ('Timestamps', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )
