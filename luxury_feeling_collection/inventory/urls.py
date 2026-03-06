from django.urls import path
from .views import stock_entry_view

app_name = 'inventory'

urlpatterns = [
    path('stock-entry/', stock_entry_view, name='stock_entry'),
]
