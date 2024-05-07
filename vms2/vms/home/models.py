from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
import json


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField(default="")
    address = models.TextField(default="")
    vendor_code = models.CharField(max_length=20, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)
    
    def __str__(self):
        """String representation of the Vendor."""
        return self.name

from django.db import models
from django.utils import timezone
import datetime

class PurchaseOrder(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    vendor = models.ForeignKey(
        'Vendor',  # If Vendor is in the same file, you can just use 'Vendor', otherwise 'app_name.ModelName'
        on_delete=models.CASCADE,
        related_name='purchase_orders'
    )
    po_number = models.CharField(max_length=20, unique=True)
    order_date = models.DateTimeField(default=timezone.now)  # Automatically set to the current time when created
    delivery_date = models.DateTimeField(null=True, blank=True)
    items = models.CharField(max_length=1000, default='{}')  # If JSON is expected, default could be '{}'
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
    expected_delivery_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'PO Number {self.po_number} - {self.vendor.name}'

    def save(self, *args, **kwargs):
        if not self.id and not self.order_date:
            # Only set if it's a new object and no date is provided
            self.order_date = timezone.now()
        super().save(*args, **kwargs)



class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE, related_name='performances')
    on_time_delivery_rate = models.FloatField(default=0.0, help_text="Percentage of on-time deliveries")
    average_quality_rating = models.FloatField(default=0.0, help_text="Average quality rating of completed orders")
    average_response_time = models.FloatField(default=0.0, help_text="Average response time in seconds")
    fulfillment_rate = models.FloatField(default=0.0, help_text="Percentage of fulfilled orders")
    quality_rating_avg = models.FloatField(default=0.0)
    # Add other fields as necessary

    def __str__(self):
        return self.name