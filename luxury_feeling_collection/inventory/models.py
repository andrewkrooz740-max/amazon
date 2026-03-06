
from django.db import models
from shop.models import Product


class StockEntry(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stock_entries')
	quantity = models.IntegerField()
	note = models.CharField(max_length=255, blank=True)
	image = models.ImageField(upload_to='inventory/', blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']
		verbose_name = 'Stock Entry'
		verbose_name_plural = 'Stock Entries'

	def __str__(self):
		return f"{self.product.name} | Qty: {self.quantity} | {self.created_at:%Y-%m-%d}" 
