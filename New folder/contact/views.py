from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ContactMessage, NewsletterSubscriber
from .serializers import ContactMessageSerializer, NewsletterSubscriberSerializer


@api_view(['POST'])
def send_message(request):
    """Submit a contact form message"""
    serializer = ContactMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Thank you for your message! We will get back to you soon.'
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def subscribe_newsletter(request):
    """Subscribe to newsletter"""
    email = request.data.get('email')
    if not email:
        return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Check if already subscribed
    if NewsletterSubscriber.objects.filter(email=email).exists():
        return Response({'message': 'You are already subscribed!'})
    
    serializer = NewsletterSubscriberSerializer(data={'email': email})
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Successfully subscribed to our newsletter!'
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
