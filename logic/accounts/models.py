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
    street_2 = models.CharField(max_length=100, blank=True, default='')
    street_3 = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()

    def __str__(self):
        retval = self.street_1
        if self.street_2 is not None and self.street_2 != '':
            retval += f', {self.street_2}'
        if self.street_3 is not None and self.street_3 != '':
            retval += f', {self.street_3}'
        return retval + f', {self.city}, {self.state} {self.zip}'



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
