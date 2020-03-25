from django.db import models
from accounts.models import ContractorProfile, ClientProfile

# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = (
        ('U', 'unclaimed'),
        ('S', 'scheduled'),
        ('F', 'finished'),
        ('C', 'canceled'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='U')
    created_at = models.DateTimeField(auto_now_add=True)
    schedule_time = models.DateTimeField(auto_now_add=True)
    contractor = models.ForeignKey(
        ContractorProfile,
        on_delete=models.PROTECT,
        related_name='jobs',
        blank=True,
        null=True
    )
    client = models.ForeignKey(
        ClientProfile,
        on_delete=models.PROTECT,
        related_name='orders'
    )
    comment = models.TextField()
