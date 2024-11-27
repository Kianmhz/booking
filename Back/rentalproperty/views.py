from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.http import JsonResponse
import uuid

from .serializers import PropertySerializer, AmenitiesSerializer, BookingSerializer, ReviewSerializer
from .models import Property, Amenities, Booking, Review, ChunkedUpload
from userarea.permissions import IsAuthenticatedUser, AllowAnyUser
from userarea.paginations import PageNumberAsLimitOffset
from userarea.functions import get_user_by_token


class PropertyViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAuthenticatedUser]
	queryset = Property.objects.all()
	serializer_class = PropertySerializer
	pagination_class = PageNumberAsLimitOffset

	def get_permissions(self):
		if self.action in ['list', 'retrieve']:
			return [AllowAnyUser()]
		return super().get_permissions()

	def get_queryset(self):
		queryset = super().get_queryset()
		if '_page' not in self.request.query_params and self.action == 'list':
			return queryset.none()
		return queryset

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()
		instance.delete()
		return Response({'message': ['Property deleted'], 'status': status.HTTP_200_OK}, status=status.HTTP_200_OK)

	def permission_denied(self, request, message=None, code=None):
		raise NotAuthenticated(message)


class AmenitiesViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAuthenticatedUser]
	queryset = Amenities.objects.all()
	serializer_class = AmenitiesSerializer
	pagination_class = PageNumberAsLimitOffset



	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()
		instance.delete()
		return Response({'message': ['Amenity deleted'], 'status': status.HTTP_200_OK}, status=status.HTTP_200_OK)

	def permission_denied(self, request, message=None, code=None):
		raise NotAuthenticated(message)


class BookingViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAuthenticatedUser]
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer
	pagination_class = PageNumberAsLimitOffset

	def get_queryset(self):
		queryset = super().get_queryset()
		if '_page' not in self.request.query_params and self.action == 'list':
			return queryset.none()
		return queryset

	def perform_create(self, serializer):
		booking = serializer.save(user=self.request.user)
		self._calculate_total_price(booking)

	def perform_update(self, serializer):
		booking = serializer.save()
		self._calculate_total_price(booking)

	def _calculate_total_price(self, booking):
		if booking.check_in and booking.check_out and booking.booking_property:
			nights = (booking.check_out - booking.check_in).days
			if nights > 0:
				booking.total_price = booking.booking_property.price * nights
				booking.save()

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()
		instance.delete()
		return Response({'message': ['Booking deleted'], 'status': status.HTTP_200_OK}, status=status.HTTP_200_OK)

	def permission_denied(self, request, message=None, code=None):
		raise NotAuthenticated(message)


class ReviewViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAuthenticatedUser]
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer

	def get_permissions(self):
		if self.action in ['list', 'retrieve']:
			return [AllowAnyUser()]
		return [IsAuthenticatedUser()]

	def get_queryset(self):
		queryset = super().get_queryset()
		property_id = self.request.query_params.get('property_id')
		if property_id:
			queryset = queryset.filter(review_property=property_id)
		return queryset

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()
		user = get_user_by_token(request)
		if user.id != instance.user.id:
			raise PermissionDenied({"detail": "You do not have permission to perform this action"})

		instance.delete()
		return Response({'message': ['Review deleted'], 'status': status.HTTP_200_OK}, status=status.HTTP_200_OK)

	def permission_denied(self, request, message=None, code=None):
		raise NotAuthenticated(message)


@csrf_exempt
def file_upload(request):
	data = request.POST
	chunk = request.FILES.get('chunk')
	upload_id = data.get('id')

	if upload_id and upload_id != 'null':
		upload = ChunkedUpload.objects.get(id=upload_id)
	else:
		filename = data.get('filename')


		randomuuid = uuid.uuid4().hex[:6]

		filename_noext = filename.split('.')[0]
		filename = f"{filename_noext}-{randomuuid}.{filename.split('.')[-1]}"

		# double check in database
		while ChunkedUpload.objects.filter(filename=filename).exists():
			filename = f"{filename_noext}-{randomuuid}.{filename.split('.')[-1]}"


		total_size = int(data.get('total_size'))
		upload = ChunkedUpload.objects.create(filename=filename, total_size=total_size)

	upload.append_chunk(chunk)
	upload.check_completion()
	domain = request.build_absolute_uri('/')[:-1]

	if upload.status == 'completed':

		return JsonResponse({
			'id': upload.id,
			'status': upload.status,
			'file_url': domain+upload.file.url
		})
	else:
		return JsonResponse({
			'id': upload.id,
			'status': upload.status,
			'offset': upload.offset,
		})