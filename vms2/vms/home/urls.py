from django.urls import path
from .views import VendorListCreateView, VendorDetailView, PurchaseOrderListCreateView, PurchaseOrderDetailView, VendorPerformanceView, VendorHistoricalPerformanceView

urlpatterns = [
    path('vendors/', VendorListCreateView.as_view(), name='vendor-list'),
    path('vendors/<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('purchase-orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list'),
    path('purchase-orders/<int:pk>/', PurchaseOrderDetailView.as_view(), name='purchase-order-detail'),
    path('vendor-performance/<int:pk>/', VendorPerformanceView.as_view(), name='vendor-performance'),
    path('historical-performance/', VendorHistoricalPerformanceView.as_view(), name='historical-performance'),
]