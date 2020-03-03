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
