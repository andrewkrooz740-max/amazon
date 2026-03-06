from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import StockEntry
from shop.models import Product

@staff_member_required
def stock_entry_view(request):
	if request.method == 'POST':
		product_id = request.POST.get('product')
		quantity = request.POST.get('quantity')
		note = request.POST.get('note', '')
		image = request.FILES.get('image')
		product = Product.objects.get(id=product_id)
		StockEntry.objects.create(product=product, quantity=quantity, note=note, image=image)
		# Optionally update product stock
		product.stock += int(quantity)
		product.save()
		return redirect('inventory:stock_entry')
	products = Product.objects.filter(is_active=True)
	stock_entries = StockEntry.objects.select_related('product').order_by('-created_at')[:20]
	return render(request, 'inventory/stock_entry.html', {
		'products': products,
		'stock_entries': stock_entries,
	})
