from django.db import models

# Users Table
class User(models.Model):
    USER_TYPE_CHOICES = [
        ('Host', 'Host'),
        ('Renter', 'Renter')
    ]

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=6, choices=USER_TYPE_CHOICES)

    def str(self):
        return self.username


# Properties Table
class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, related_name='properties', on_delete=models.CASCADE)
    property_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    property_description = models.TextField()
    amenity_id = models.AutoField(primary_key=True)

    def str(self):
        return self.property_name


# Bookings Table
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, related_name='bookings', on_delete=models.CASCADE)
    renter = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def str(self):
        return f"Booking {self.booking_id}"


# Reviews Table
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()

def str(self):
        return f"Review for {self.property.property_name} by {self.user.username}"


# Payments Table
class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed')
    ]

    payment_id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, related_name='payments', on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES)

    def str(self):
        return f"Payment {self.payment_id} for Booking {self.booking.booking_id}"


# Amenities Table
class Amenity(models.Model):
    amenity_id = models.AutoField(primary_key=True)
    amenity_name = models.CharField(max_length=100)

    def str(self):
        return self.amenity_name




# Sample Data Insertion
# You would insert sample data like this (adjust it as per Django shell or admin interface)
# from your_app.models import User, Property, Booking, Review, Payment, Amenity
# Example of creating a user
# user = User.objects.create(username='host1', email='host1@example.com', password='password1', user_type='Host')
# # Add more users, properties, bookings, etc. in a similar way.

