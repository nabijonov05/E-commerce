from django.urls import path
from apps.orders.api_endpoints.orders.OrderList.views import OrderListAPIView
from apps.orders.api_endpoints.orders.OrderCreate.views import OrderCreateAPIView
from apps.orders.api_endpoints.orders.OrderDetail.views import OrderDetailAPIView
from apps.orders.api_endpoints.orders.OrderUpdateDestroy.views import OrderUpdateAPIView, OrderDestroyAPIview

urlpatterns = [
    path('orders/', OrderListAPIView.as_view(), name='order_list'),
    path('create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('<int:pk>/', OrderDetailAPIView.as_view(), name='order-detail'),
    path('<int:pk>/update/', OrderUpdateAPIView.as_view(), name='order-update'),
    path('<int:pk>/delete/', OrderDestroyAPIview.as_view(), name='order-delete'),
]