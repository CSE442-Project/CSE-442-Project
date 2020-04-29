from django.db import models
from django.contrib.auth.models import User


class ContractorProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='contractor_profile'
    )
    phone = models.BigIntegerField()
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class ContractorVehicle(models.Model):
    # owner = models.ForeignKey(
    #     ContractorProfile,
    #     on_delete=models.CASCADE,
    #     related_name='vehicles'
    # )
    vehicleMake = models.CharField(max_length=50)
    vehicleModel = models.CharField(max_length=50)
    vehicleLicense = models.CharField(max_length=50)
    

    def __str__(self):
        return f'{self.vehicleMake},{self.vehicleMake},{self.vehicleLicense}'


class Address(models.Model):
    street_1 = models.CharField(max_length=100)
    street_2 = models.CharField(max_length=100, blank=True, default='')
    street_3 = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()

    def __str__(self):
        return f'{self.street_1}, {self.street_2}, {self.street_3}, {self.city}, {self.state} {self.zip}'


class ClientProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='client_profile'
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name='client_profiles'
    )
    phone = models.BigIntegerField()
    dw_size = models.IntegerField()

    def __str__(self):
        return self.user.username
