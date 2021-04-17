from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

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

order_status = [
    ('pending', 'pending'),
    ('confirmed', 'confirmed'),
    ('processing', 'processing'),
    ('delivered', 'delivered'),
]

nozzles = [
    ('single', 'Single'),
    ('double', 'Double'),
]

display = [
    ('touch', 'Touch'),
    ('knob', 'Knob'),
    ('touch+knob', 'Touch + Knob'),
]

motor_driver = [
    ('normal', 'Normal'),
    ('silent', 'Silent'),
]

cover = [
    ('yes', 'Yes'),
    ('no', 'No'),
]

filament_chamber = [
    ('yes', 'Yes'),
    ('no', 'No'),
]

ups = [
    ('yes', 'Yes'),
    ('no', 'No'),
]

abl_support = [
    ('yes', 'Yes'),
    ('no', 'No'),
]

wifi_support = [
    ('yes', 'Yes'),
    ('no', 'No'),
]

filament_q = [
    ('1kg', '1kg'),
    ('2kg', '2kg'),
    ('3kg', '3kg'),
]

bed_size = [
    ('220x220', '220x220'),
    ('300x300', '300x300'),
    ('440x440', '440x440'),
    ('600x600', '600x600'),
]

class BestOffers(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    bed_size = models.CharField(max_length=100, choices=bed_size, default='220x220')
    height = models.CharField(max_length=100, default='')
    feature1 = models.CharField(max_length=100, default='')
    feature2 = models.CharField(max_length=100, default='')
    feature3 = models.CharField(max_length=100, default='')
    nozzle = models.CharField(max_length=100, choices=nozzles, default='single')
    display = models.CharField(max_length=100, choices=display, default='knob')
    motor_driver_type = models.CharField(max_length=100, choices=motor_driver, default='normal')
    cover = models.CharField(max_length=100, choices=cover, default='no')
    filament_chamber = models.CharField(max_length=100, choices=filament_chamber, default='no')
    ups_module = models.CharField(max_length=100, choices=ups, default='no')
    abl = models.CharField(max_length=100, choices=abl_support, default='no')
    wifi = models.CharField(max_length=100, choices=wifi_support, default='no')
    filament = models.CharField(max_length=100, choices=filament_q, default='1kg')
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


class ProfileInfo(models.Model):
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


class Orders(models.Model):
    title = models.CharField(max_length=100)
    order_time = models.DateTimeField(default=timezone.now)
    bed_size = models.CharField(max_length=100, default='')
    height = models.CharField(max_length=100, default='')
    nozzle = models.CharField(max_length=100, choices=nozzles, default='single')
    display = models.CharField(max_length=100, choices=display, default='knob')
    motor_driver_type = models.CharField(max_length=100, choices=motor_driver, default='normal')
    cover = models.CharField(max_length=100, choices=cover, default='no')
    filament_chamber = models.CharField(max_length=100, choices=filament_chamber, default='no')
    ups_module = models.CharField(max_length=100, choices=ups, default='no')
    abl = models.CharField(max_length=100, choices=abl_support, default='no')
    wifi = models.CharField(max_length=100, choices=wifi_support, default='no')
    filament = models.CharField(max_length=100, choices=filament_q, default='1kg')
    price = models.IntegerField()
    discount_price = models.IntegerField(null=True)
    order_status = models.CharField(max_length=100, choices=order_status, default='pending')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class BedSize(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    lowest_height = models.IntegerField()
    highest_height = models.IntegerField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Height(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Covered(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class ABL(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class WiFi(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class FilamentChamber(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)