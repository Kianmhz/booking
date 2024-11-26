from rest_framework import serializers
from .models import User, Property, Booking, Review, Payment, Amenity, PropertyAmenity

# Serializer for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'user_type']

# Serializer for Property model
class PropertySerializer(serializers.ModelSerializer):
    owner = UserSerializer()  # Nested serializer for owner (User)

    class Meta:
        model = Property
        fields = ['property_id', 'owner', 'property_name', 'location', 'price_per_night', 'property_description', 'amenity_id']

# Serializer for Booking model
class BookingSerializer(serializers.ModelSerializer):
    property = PropertySerializer()  # Nested serializer for property (Property)
    renter = UserSerializer()  # Nested serializer for renter (User)

    class Meta:
        model = Booking
        fields = ['booking_id', 'property', 'renter', 'check_in_date', 'check_out_date', 'total_price']

# Serializer for Review model
class ReviewSerializer(serializers.ModelSerializer):
    property = PropertySerializer()  # Nested serializer for property (Property)
    user = UserSerializer()  # Nested serializer for user (User)

    class Meta:
        model = Review
        fields = ['review_id', 'property', 'user', 'rating', 'comment']

# Serializer for Payment model
class PaymentSerializer(serializers.ModelSerializer):
    booking = BookingSerializer()  # Nested serializer for booking (Booking)

    class Meta:
        model = Payment
        fields = ['payment_id', 'booking', 'payment_date', 'amount', 'payment_status']

# Serializer for Amenity model
class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['amenity_id', 'amenity_name']

