from django.urls import path, include
from rest_framework import routers

from .views import PropertyViewSet, AmenitiesViewSet, BookingViewSet, ReviewViewSet, file_upload

app_name = "user_area"
router = routers.SimpleRouter()
router.register('properties', PropertyViewSet, basename='properties')
router.register('amenities', AmenitiesViewSet, basename='amenities')
router.register('booking', BookingViewSet, basename='booking')
router.register('review', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
    path('file-upload/', file_upload, name='large-file-chunked-upload'),

]
