from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'email', 'city', 'total', 'status', 'paid', 'created_at']
    list_filter = ['status', 'paid', 'created_at']
    list_editable = ['status', 'paid']
    search_fields = ['first_name', 'last_name', 'email', 'address']
    date_hierarchy = 'created_at'
    inlines = [OrderItemInline]
    ordering = ['-created_at']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product_name', 'price', 'quantity', 'get_cost']
    list_filter = ['order']

    def get_cost(self, obj):
        return obj.get_cost()
    get_cost.short_description = 'Total'
