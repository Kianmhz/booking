from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.core.files.base import ContentFile
from django.db import models
import os

from userarea.models import User


class ChunkedUpload(models.Model):

    STATUS_CHOICES = [
        ('started', 'Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    filename = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    offset = models.BigIntegerField(default=0)
    total_size = models.BigIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='started')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def append_chunk(self, chunk):
        try:
            # If chunk is an InMemoryUploadedFile or TemporaryUploadedFile, read the data
            if isinstance(chunk, (InMemoryUploadedFile, TemporaryUploadedFile)):
                chunk = chunk.read()

            if self.file:
                # If a file has already been uploaded, append the chunk to it
                with open(self.file.path, 'ab') as destination:
                    # Seek to the end of the file to append the new chunk
                    destination.seek(0, os.SEEK_END)
                    destination.write(chunk)
            else:
                # If no file has been uploaded yet, create a new file with the chunk
                self.file.save(self.filename, ContentFile(chunk))

            # Update the offset
            self.offset = self.file.size
            self.save()

        except Exception as e:
            self.status = 'failed'
            self.save()
            raise e


    def check_completion(self):
        if self.offset >= self.total_size:
            self.status = 'completed'
            self.save()

    def __str__(self):
        return self.filename


# delete the file when the ChunkedUpload object is deleted
@receiver(pre_delete, sender=ChunkedUpload)
def delete_file(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete(save=False)



class Property(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_properties', null=True, blank=True)
	title = models.CharField(max_length=255, null=True, blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	location = models.TextField(null=True, blank=True)
	description = models.TextField()
	media = models.ManyToManyField(ChunkedUpload, related_name='property_media', blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.id}-{self.title}"

	class Meta:
		verbose_name = 'Property'
		verbose_name_plural = 'Properties'


class Booking(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bookings', null=True, blank=True)
	booking_property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_bookings', null=True, blank=True)
	check_in = models.DateField()
	check_out = models.DateField()
	total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

	def __str__(self):
		return f"{self.id}"


class Review(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reviews', null=True, blank=True)
	review_property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_reviews', null=True, blank=True)
	rating = models.IntegerField()
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.id}"


class Amenities(models.Model):
	amenities_property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_options', null=True, blank=True)
	key = models.CharField(max_length=255)
	value = models.TextField()

	def __str__(self):
		return f"{self.id}"

	class Meta:
		verbose_name = 'Amenity'
		verbose_name_plural = 'Amenities'
