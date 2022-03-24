from django.contrib import admin
from .Models.products import Product
from .Models.category import Category


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'image']


class AdminCategory(admin.ModelAdmin):
    list_display = ['description']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
