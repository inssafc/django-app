from django.contrib import admin
from .models import Category, Product, Order, OrderItem, Cart, CartItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'description']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'total_price', 'is_completed']
    list_filter = ['is_completed', 'created_at']
    inlines = [OrderItemInline]

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'session_id', 'created_at']
    inlines = [CartItemInline]