from rest_framework import serializers

from .models import Property, Amenities, Booking, Review
from userarea.functions import get_user_by_token


class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenities
        fields = ['id', 'amenities_property', 'key', 'value']


class PropertySerializer(serializers.ModelSerializer):
	property_options = AmenitiesSerializer(many=True, read_only=True)

	def to_representation(self, instance):
		data = super().to_representation(instance)
		if 'media' in data:
			request = self.context.get('request')
			if request:
				data['media'] = [
					{
						'id': media.id,
						'link': request.build_absolute_uri(media.file.url)
					}
					for media in instance.media.all()
				]
		return data

	class Meta:
		model = Property
		fields = [
			'id', 'title', 'user', 'price', 'location',
			'description', 'media', 'created_at',
			'updated_at', 'property_options'
		]

	def validate(self, data):
		user = get_user_by_token(self.context['request'])
		if data['price'] < 0:
			raise serializers.ValidationError("Price cannot be less than 0")

		if user.user_type != 2:
			raise serializers.ValidationError({"detail": "Only hosts can create properties"})

		return data


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = '__all__'

	def validate(self, data):
		user = get_user_by_token(self.context['request'])
		if user.user_type != 1:
			raise serializers.ValidationError({"detail": "Only customer can create bookings"})

		return data


class ReviewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Review
		fields = '__all__'

	def validate(self, data):
		user = get_user_by_token(self.context['request'])
		rating = data.get('rating')
		if user.user_type != 1:
			raise serializers.ValidationError({"detail": "Only customer can create reviews"})

		if rating < 1 or rating > 5:
			raise serializers.ValidationError({"detail": "Rating must be between 1 and 5"})
		return data
