from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.ContractorProfile)
admin.site.register(models.ContractorVehicle)
admin.site.register(models.ClientProfile)
admin.site.register(models.Address)
