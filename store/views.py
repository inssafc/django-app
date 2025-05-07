from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Category, Order, OrderItem
from .cart import add_to_cart, remove_from_cart, get_cart_items, get_cart_total, clear_cart

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'store/home.html', {'products': products, 'categories': categories})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category_products.html', {'category': category, 'products': products})

def add_to_cart_view(request, product_id):
    quantity = int(request.POST.get('quantity', 1))
    add_to_cart(request, product_id, quantity)
    messages.success(request, "Produit ajouté au panier avec succès!")
    return redirect('product_detail', product_id=product_id)

def remove_from_cart_view(request, product_id):
    remove_from_cart(request, product_id)
    messages.success(request, "Produit retiré du panier!")
    return redirect('view_cart')

def view_cart(request):
    cart_items = get_cart_items(request)
    total = get_cart_total(request)
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def checkout(request):
    cart_items = get_cart_items(request)
    total = get_cart_total(request)
    
    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            total_price=total
        )
        
        # Ajouter les éléments du panier à la commande
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        
        clear_cart(request)
        
        messages.success(request, "Commande effectuée avec succès!")
        return redirect('home')
    
    return render(request, 'store/checkout.html', {'cart_items': cart_items, 'total': total})

def product_catalog(request):
    backpacks = Product.objects.filter(category__name='Sacs à dos')
    return render(request, 'store/catalog.html', {'products': backpacks})