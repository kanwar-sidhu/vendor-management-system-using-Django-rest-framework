# vendor_api/views.py
from datetime import timezone
from rest_framework import generics
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer

# Vendor Views
class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

# Purchase Order Views
class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

# Historical Performance View
class VendorHistoricalPerformanceView(generics.ListCreateAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer

# Vendor Performance View
class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def get_object(self):
        """
        Override the get_object method to fetch the vendor along with their updated performance metrics
        """
        vendor_id = self.kwargs.get('pk')        
        return generics.get_object_or_404(Vendor, pk=vendor_id)

# Purchase Order Acknowledgment View
class PurchaseOrderAcknowledgmentView(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def perform_update(self, serializer):
        # Acknowledge the order by setting the current timestamp to acknowledgment_date
        serializer.save(acknowledgment_date=timezone.now())
