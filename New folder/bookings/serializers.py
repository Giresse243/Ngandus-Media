from rest_framework import serializers
from .models import BookingRequest


class BookingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingRequest
        fields = ['id', 'name', 'email', 'phone', 'service', 'preferred_date', 'preferred_time', 'message']
        read_only_fields = ['id']
