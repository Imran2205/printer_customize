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
    ('Single', 'Single'),
    ('Double', 'Double'),
]

display = [
    ('Touch', 'Touch'),
    ('Knob', 'Knob'),
    ('Touch + Knob', 'Touch + Knob'),
]

motor_driver = [
    ('Normal', 'Normal'),
    ('Silent', 'Silent'),
]

yes_or_no = [
    ('No', 'No'),
    ('Yes', 'Yes'),
]

filament_q = [
    ('1kg', '1kg'),
    ('2kg', '2kg'),
    ('3kg', '3kg'),
]

bed_size = [
    ('220 X 220', '220 X 220'),
    ('300 X 300', '300 X 300'),
    ('400 X 400', '400 X 400'),
    ('440 X 440', '440 X 440'),
    ('600 X 600', '600 X 600'),
]

height = [
    ('200', '200'),
    ('250', '250'),
    ('300', '300'),
    ('350', '350'),
    ('400', '400'),
    ('450', '450'),
    ('500', '500'),
    ('550', '550'),
    ('600', '600'),
    ('650', '650'),
    ('700', '700'),
]

class BestOffers(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    bed_size = models.CharField(max_length=100, choices=bed_size, default='220x220')
    height = models.CharField(max_length=100, choices=height, default='200')
    feature1 = models.CharField(max_length=100, default='')
    feature2 = models.CharField(max_length=100, default='')
    feature3 = models.CharField(max_length=100, default='')
    nozzle = models.CharField(max_length=100, choices=nozzles, default='single')
    display = models.CharField(max_length=100, choices=display, default='knob')
    motor_driver_type = models.CharField(max_length=100, choices=motor_driver, default='normal')
    cover = models.CharField(max_length=100, choices=yes_or_no, default='no')
    filament_chamber = models.CharField(max_length=100, choices=yes_or_no, default='no')
    ups_module = models.CharField(max_length=100, choices=yes_or_no, default='no')
    abl = models.CharField(max_length=100, choices=yes_or_no, default='no')
    wifi = models.CharField(max_length=100, choices=yes_or_no, default='no')
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
    bed_size = models.CharField(max_length=100, choices=bed_size, default='220x220')
    height = models.CharField(max_length=100, choices=height, default='200')
    nozzle = models.CharField(max_length=100, choices=nozzles, default='single')
    display = models.CharField(max_length=100, choices=display, default='knob')
    motor_driver_type = models.CharField(max_length=100, choices=motor_driver, default='normal')
    cover = models.CharField(max_length=100, choices=yes_or_no, default='no')
    filament_chamber = models.CharField(max_length=100, choices=yes_or_no, default='no')
    ups_module = models.CharField(max_length=100, choices=yes_or_no, default='no')
    abl = models.CharField(max_length=100, choices=yes_or_no, default='no')
    wifi = models.CharField(max_length=100, choices=yes_or_no, default='no')
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
    title = models.CharField(max_length=100, choices=bed_size, default='220x220')
    price = models.IntegerField()
    lowest_height = models.IntegerField()
    highest_height = models.IntegerField()
    field_name = models.CharField(max_length=100, default="bed_size")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Height(models.Model):
    title = models.CharField(max_length=100, choices=height, default='200')
    bed_size = models.CharField(max_length=100, choices=bed_size, default='220x220')
    price = models.IntegerField()
    field_name = models.CharField(max_length=100, default="height")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Nozzle(models.Model):
    title = models.CharField(max_length=100, choices=nozzles, default='single')
    price = models.IntegerField()
    field_name = models.CharField(max_length=100, default="nozzle")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Display(models.Model):
    title = models.CharField(max_length=100, choices=display, default='knob')
    price = models.IntegerField()
    field_name = models.CharField(max_length=100, default="display")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class UPSModule(models.Model):
    title = models.CharField(max_length=100, choices=yes_or_no, default='no')
    price = models.IntegerField()
    field_name = models.CharField(max_length=100, default="ups")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class MotorDriver(models.Model):
    title = models.CharField(max_length=100, choices=motor_driver, default='normal')
    price = models.IntegerField()
    field_name = models.CharField(max_length=100, default="motor_driver")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Covered(models.Model):
    title = models.CharField(max_length=100, choices=yes_or_no, default='no')
    price = models.IntegerField()
    field_name = models.CharField(max_length=100, default="cover")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class ABL(models.Model):
    title = models.CharField(max_length=100, choices=yes_or_no, default='no')
    price = models.IntegerField()
    field_name = models.CharField(max_length=100, default="abl")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class WiFi(models.Model):
    title = models.CharField(max_length=100, choices=yes_or_no, default='no')
    price = models.IntegerField()
    field_name = models.CharField(max_length=100, default="wifi")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class FilamentChamber(models.Model):
    title = models.CharField(max_length=100, choices=yes_or_no, default='no')
    price = models.IntegerField()
    field_name = models.CharField(max_length=100, default="filament_chamber")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class FilamentQuantity(models.Model):
    title = models.CharField(max_length=100, choices=filament_q, default='1kg')
    price = models.IntegerField()
    field_name = models.CharField(max_length=100, default="filament_quantity")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Image(models.Model):
    offer = models.OneToOneField(BestOffers, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.offer.title + "_image"