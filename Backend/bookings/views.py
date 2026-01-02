from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BookingRequest
from .serializers import BookingRequestSerializer


@api_view(['POST'])
def create_booking(request):
    """Create a new booking request"""
    serializer = BookingRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Booking request submitted successfully!',
            'booking': serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_services_list(request):
    """Get list of available services for booking form"""
    from content.models import Service
    services = Service.objects.values_list('title', flat=True)
    return Response(list(services))
