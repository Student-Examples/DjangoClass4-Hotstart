from django.contrib.admin import site, ModelAdmin

from products.models import Product, Category


class CategoryAdmin(ModelAdmin):
    list_display = ["name", "description", "is_active", "created_date"]


class ProductAdmin(ModelAdmin):
    list_display = ["name", "price", "count", "created_date"]


site.register(Category, CategoryAdmin)
site.register(Product, ProductAdmin)
