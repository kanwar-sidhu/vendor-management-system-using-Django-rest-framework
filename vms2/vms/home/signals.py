# vendor_api/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg, F
from .models import PurchaseOrder, Vendor,HistoricalPerformance
from django.db.models import Count, Q

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance(sender, instance, created, **kwargs):
    vendor = instance.vendor
    if instance.status == 'completed':
        update_on_time_delivery_rate(vendor)
        update_quality_rating_average(vendor)
    if instance.acknowledgment_date is not None:
        update_average_response_time(vendor)
    update_fulfillment_rate(vendor)

def update_on_time_delivery_rate(vendor):
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    total = completed_pos.count()
    on_time = completed_pos.filter(delivery_date__lte=F('expected_delivery_date')).count()
    vendor.on_time_delivery_rate = on_time / total if total > 0 else 0
    vendor.save()

def update_quality_rating_average(vendor):
    result = PurchaseOrder.objects.filter(vendor=vendor, status='completed', quality_rating__isnull=False).aggregate(avg_rating=Avg('quality_rating'))
    vendor.average_quality_rating = result['avg_rating'] if result['avg_rating'] is not None else 0
    vendor.save()

def update_average_response_time(vendor):
    acknowledged_pos = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
    if acknowledged_pos.exists():
        total_response_time = sum((po.acknowledgment_date - po.issue_date).total_seconds() for po in acknowledged_pos)
        vendor.average_response_time = total_response_time / acknowledged_pos.count()
    else:
        vendor.average_response_time = 0
    vendor.save()

def update_fulfillment_rate(vendor):
    all_pos = PurchaseOrder.objects.filter(vendor=vendor)
    total = all_pos.count()
    completed = all_pos.filter(status='completed').count()
    vendor.fulfillment_rate = completed / total if total > 0 else 0
    vendor.save()
