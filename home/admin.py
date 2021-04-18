from django.contrib import admin
from django.contrib import admin
from .models import ProfileInfo, BestOffers, Orders, BedSize, Height, Nozzle, Display, Covered, ABL, FilamentQuantity, FilamentChamber, WiFi, MotorDriver, UPSModule

admin.site.register(ProfileInfo)
admin.site.register(BestOffers)
admin.site.register(Orders)
admin.site.register(BedSize)
admin.site.register(Height)
admin.site.register(Nozzle)
admin.site.register(Display)
admin.site.register(Covered)
admin.site.register(ABL)
admin.site.register(FilamentQuantity)
admin.site.register(FilamentChamber)
admin.site.register(WiFi)
admin.site.register(MotorDriver)
admin.site.register(UPSModule)
