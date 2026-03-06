from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib import messages
from .models import NewsletterSubscriber


@require_POST
def subscribe(request):
    email = request.POST.get('email', '').strip()
    if email:
        subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)
        if created:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'status': 'success', 'message': 'Thank you for subscribing!'})
            messages.success(request, 'Thank you for subscribing!')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'status': 'info', 'message': 'You are already subscribed.'})
            messages.info(request, 'You are already subscribed.')
    else:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'status': 'error', 'message': 'Please enter a valid email.'})
        messages.error(request, 'Please enter a valid email.')
    
    return redirect(request.META.get('HTTP_REFERER', '/'))
