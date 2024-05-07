from django.contrib import admin
from .models import Vendor, PurchaseOrder, HistoricalPerformance

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'name', 
        'contact_details', 
        'address', 
        'vendor_code',
        'on_time_delivery_rate', 
        'quality_rating', 
        'average_response_time', 
        'fulfillment_rate'
    )

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'po_number', 
        'vendor_reference_display', 
        'order_date', 
        'items',
        'quantity', 
        'status', 
        'quality_rating', 
        'issue_date', 
        'acknowledgment_date', 
        'vendor'
    )

    def vendor_reference_display(self, obj):
        # Provides a reference to the vendor's code if available.
        return obj.vendor.vendor_code if obj.vendor else ''
    vendor_reference_display.short_description = 'Vendor Code'

@admin.register(HistoricalPerformance)
class HistoricalPerformanceAdmin(admin.ModelAdmin):
    # Assuming 'date' is intended to be the date of the record creation or another significant date
    # You need to ensure the HistoricalPerformance model has a field named 'date' or change this to a correct field
    list_display = (
        'vendor',  # Assumed correction: replacing 'date' with 'name' or ensure 'date' is defined in the model.
        'on_time_delivery_rate',
        'quality_rating_avg',
        'average_response_time',
        'fulfillment_rate'
    )
