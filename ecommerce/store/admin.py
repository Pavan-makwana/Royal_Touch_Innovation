from django.contrib import admin
from .models import ProductRequest
from .models import Category, Product, ProductRequest

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]
    list_filter = ["category"]

@admin.register(ProductRequest)
class ProductRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "product", "phone", "created_at")
    search_fields = ("name", "phone", "product__name")
    list_filter = ("created_at",)

