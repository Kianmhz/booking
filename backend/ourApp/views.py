from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import User, Property, Booking, Review, Payment, Amenity, PropertyAmenity
from .serializers import UserSerializer, PropertySerializer, BookingSerializer, ReviewSerializer, PaymentSerializer, AmenitySerializer, PropertyAmenitySerializer

# User Views
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Property Views
class PropertyListCreate(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

# Booking Views
class BookingListCreate(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# Review Views
class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Payment Views
class PaymentListCreate(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

# Amenity Views
class AmenityListCreate(generics.ListCreateAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

class AmenityRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

# Property Amenity Views
class PropertyAmenityListCreate(generics.ListCreateAPIView):
    queryset = PropertyAmenity.objects.all()
    serializer_class = PropertyAmenitySerializer

class PropertyAmenityRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyAmenity.objects.all()
    serializer_class = PropertyAmenitySerializer