from django.contrib import admin

from .models import ChunkedUpload, Property, Booking, Review, Amenities


@admin.register(ChunkedUpload)
class ChunkedUploadAdmin(admin.ModelAdmin):
	list_display = ('id','filename', 'status', 'created_at')
	list_filter = ('status', 'created_at')
	search_fields = ('filename', 'status', 'created_at')


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
	list_display = ('id','title', 'user', 'price', 'created_at')
	list_filter = ('user', 'created_at')
	search_fields = ('title', 'user', 'price', 'created_at')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
	list_display = ('id','user', 'booking_property', 'check_in', 'check_out', 'total_price')
	list_filter = ('user', 'booking_property', 'check_in', 'check_out')
	search_fields = ('user', 'booking_property', 'check_in', 'check_out', 'total_price')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
	list_display = ('id','user', 'review_property', 'rating', 'created_at')
	list_filter = ('user', 'review_property', 'rating', 'created_at')
	search_fields = ('user', 'review_property', 'rating', 'created_at')


@admin.register(Amenities)
class AmenitiesAdmin(admin.ModelAdmin):
	list_display = ('id','amenities_property', 'key', 'value')
	list_filter = ('amenities_property', 'key')
	search_fields = ('amenities_property', 'key', 'value')
