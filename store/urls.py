from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart_view, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart_view, name='remove_from_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('catalog/', views.product_catalog, name='product_catalog'),
]