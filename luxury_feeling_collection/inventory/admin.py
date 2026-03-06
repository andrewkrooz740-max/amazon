from django.contrib import admin
from .models import StockEntry

@admin.register(StockEntry)
class StockEntryAdmin(admin.ModelAdmin):
	list_display = ('product', 'quantity', 'note', 'created_at')
	list_filter = ('product', 'created_at')
	search_fields = ('product__name', 'note')
