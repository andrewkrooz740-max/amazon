from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, DetailView
from django.contrib import messages
from cart.cart import Cart
from .models import Order, OrderItem
from .forms import OrderCreateForm


class CheckoutView(View):
    template_name = 'orders/checkout.html'

    def get(self, request):
        cart = Cart(request)
        if len(cart) == 0:
            messages.warning(request, 'Your cart is empty.')
            return redirect('shop:product_list')
        
        form = OrderCreateForm()
        if request.user.is_authenticated:
            profile = getattr(request.user, 'profile', None)
            if profile:
                form = OrderCreateForm(initial={
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'email': request.user.email,
                    'phone': profile.phone,
                    'address': profile.address,
                    'city': profile.city,
                    'country': profile.country,
                })
            else:
                form = OrderCreateForm(initial={
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'email': request.user.email,
                })
        
        return render(request, self.template_name, {'cart': cart, 'form': form})

    def post(self, request):
        cart = Cart(request)
        if len(cart) == 0:
            messages.warning(request, 'Your cart is empty.')
            return redirect('shop:product_list')
        
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.total = cart.get_total_price()
            order.save()
            
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    product_name=item['product'].name,
                    price=item['price'],
                    quantity=item['quantity']
                )
            
            cart.clear()
            messages.success(request, f'Order #{order.id} placed successfully!')
            return redirect('orders:order_complete', order_id=order.id)
        
        return render(request, self.template_name, {'cart': cart, 'form': form})


class OrderCompleteView(DetailView):
    model = Order
    template_name = 'orders/order_complete.html'
    context_object_name = 'order'
    pk_url_kwarg = 'order_id'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            return qs.filter(user=self.request.user) | qs.filter(email=self.request.user.email)
        return qs
