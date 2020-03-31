from django.db import models
from django.contrib.auth.models import User

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
    schedule_time = models.DateTimeField(blank=True, null=True)
    contractor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='contractor_jobs',
        blank=True,
        null=True
    )
    client = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='client_orders'
    )
    comment = models.TextField(blank=True, null=True)
