from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, ProductImage, ProductColor


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductColorInline(admin.TabularInline):
    model = ProductColor
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'thumbnail', 'slug', 'position', 'is_active', 'product_count']
    list_editable = ['position', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    list_filter = ['is_active']

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover;border-radius:50%;"/>', obj.image.url)
        return '-'
    thumbnail.short_description = 'Image'

    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = 'Products'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'thumbnail', 'category', 'price', 'stock', 'is_featured', 'is_new', 'is_bestseller', 'is_active']
    list_editable = ['price', 'stock', 'is_featured', 'is_new', 'is_bestseller', 'is_active']
    list_filter = ['category', 'is_featured', 'is_new', 'is_bestseller', 'is_active']
    search_fields = ['name', 'description', 'material']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, ProductColorInline]
    date_hierarchy = 'created_at'

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="60" style="object-fit:cover;border-radius:4px;"/>', obj.image.url)
        return '-'
    thumbnail.short_description = 'Image'


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'thumbnail', 'position']
    list_editable = ['position']
    list_filter = ['product']

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover;"/>', obj.image.url)
        return '-'
