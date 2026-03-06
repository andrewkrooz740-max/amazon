from django.shortcuts import render
from django.views.generic import TemplateView
from shop.models import Product, Category
from .models import FeaturedCollection, HeroSlide


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(is_active=True)[:5]
        context['featured_products'] = Product.objects.filter(is_featured=True, is_active=True)[:4]
        context['new_arrivals'] = Product.objects.filter(is_new=True, is_active=True)[:4]
        context['hero_slides'] = HeroSlide.objects.filter(is_active=True)
        context['featured_collections'] = FeaturedCollection.objects.filter(is_active=True)[:3]
        return context


class SearchView(TemplateView):
    template_name = 'core/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        context['query'] = query
        if query:
            context['products'] = Product.objects.filter(
                is_active=True
            ).filter(
                models.Q(name__icontains=query) |
                models.Q(description__icontains=query) |
                models.Q(category__name__icontains=query)
            ).distinct()
        else:
            context['products'] = Product.objects.none()
        return context


from django.db import models  # noqa


class SearchView(TemplateView):
    template_name = 'core/search.html'

    def get_context_data(self, **kwargs):
        from django.db.models import Q
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        context['query'] = query
        if query:
            context['products'] = Product.objects.filter(
                is_active=True
            ).filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
            ).distinct()
        else:
            context['products'] = Product.objects.none()
        return context
