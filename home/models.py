from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

stat2 = [
    ('not_verified', 'not_verified'),
    ('verified', 'verified'),
    ('pending', 'pending'),
    ('new', 'new'),
]

DIV = [
    ('dhaka', 'Dhaka'),
    ('rajshahi', 'Rajshahi'),
    ('rangpur', 'Rangpur'),
    ('sylhet', 'Sylhet'),
    ('khulna', 'Khulna'),
    ('chittagong', 'Chittagong'),
    ('barishal', 'Barishal'),
]

class BestOffers(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    motor_driver_type = models.BooleanField()
    cover = models.BooleanField()
    filament_chamber = models.BooleanField()
    ups_module = models.BooleanField()
    abl = models.BooleanField()
    wifi = models.BooleanField()
    price = models.IntegerField()
    discount_price = models.IntegerField(null=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

"""class PriceDB(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)"""

class Profile_info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=100, choices=DIV)
    zip = models.CharField(max_length=20)
    phone = PhoneNumberField()
    profile_status = models.CharField(max_length=100, choices=stat2, default='new')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)