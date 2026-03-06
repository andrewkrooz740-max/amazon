from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.CheckoutView.as_view(), name='checkout'),
    path('complete/<int:order_id>/', views.OrderCompleteView.as_view(), name='order_complete'),
]
