from django.db import models
from django.contrib.auth.models import User


class ContractorProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='contractor_profile'
    )
    phone = models.IntegerField()

    def __str__(self):
        return self.user.username


class ContractorVehicle(models.Model):
    owner = models.ForeignKey(
        ContractorProfile,
        on_delete=models.CASCADE,
        related_name='vehicles'
    )
    color = models.CharField(max_length=20)
    plate = models.CharField(max_length=7)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return self.plate


class Address(models.Model):
    street_1 = models.CharField(max_length=100)
    street_2 = models.CharField(max_length=100)
    street_3 = models.CharField(max_length=100)
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
    phone = models.IntegerField()
    dw_size = models.IntegerField()

    def __str__(self):
        return self.user.username
