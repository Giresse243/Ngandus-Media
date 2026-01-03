from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import BookingRequest
from .serializers import BookingRequestSerializer


@api_view(['POST'])
def create_booking(request):
    """Create a new booking request"""
    serializer = BookingRequestSerializer(data=request.data)
    if serializer.is_valid():
        booking = serializer.save()
        
        # Send email notification to admin
        try:
            admin_subject = f'New Booking Request - {booking.service}'
            admin_message = f"""
New booking request received from Ngandus Media website:

Client: {booking.name}
Email: {booking.email}
Phone: {booking.phone}
Service: {booking.service}
Preferred Date: {booking.preferred_date}
Preferred Time: {booking.preferred_time}
Message: {booking.message}

Status: {booking.status}
Booking ID: {booking.id}
            """
            send_mail(
                admin_subject,
                admin_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=True,
            )
            
            # Send confirmation email to client
            client_subject = 'Booking Request Received - Ngandus Media'
            client_message = f"""
Dear {booking.name},

Thank you for your booking request!

We have received your request for {booking.service} on {booking.preferred_date} at {booking.preferred_time}.

Our team will review your request and get back to you within 24 hours.

Booking Details:
- Service: {booking.service}
- Date: {booking.preferred_date}
- Time: {booking.preferred_time}

If you have any questions, please contact us at {settings.ADMIN_EMAIL} or +27 XX XXX XXXX.

Best regards,
Ngandus Media Team
            """
            send_mail(
                client_subject,
                client_message,
                settings.DEFAULT_FROM_EMAIL,
                [booking.email],
                fail_silently=True,
            )
        except Exception as e:
            # Log error but don't fail the booking
            print(f"Email error: {e}")
        
        return Response({
            'message': 'Booking request submitted successfully! Check your email for confirmation.',
            'booking': serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_services_list(request):
    """Get list of available services for booking form"""
    from content.models import Service
    services = Service.objects.values_list('title', flat=True)
    return Response(list(services))
