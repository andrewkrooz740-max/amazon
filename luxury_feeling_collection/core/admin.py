from django.contrib import admin
from django.utils.html import format_html
from .models import FeaturedCollection, HeroSlide


@admin.register(FeaturedCollection)
class FeaturedCollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'thumbnail', 'position', 'is_active', 'created_at']
    list_editable = ['position', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['is_active']
    search_fields = ['name', 'description']

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover;border-radius:4px;"/>', obj.image.url)
        return '-'
    thumbnail.short_description = 'Image'


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'thumbnail', 'position', 'is_active']
    list_editable = ['position', 'is_active']
    list_filter = ['is_active']

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" height="40" style="object-fit:cover;border-radius:4px;"/>', obj.image.url)
        return '-'
    thumbnail.short_description = 'Image'
