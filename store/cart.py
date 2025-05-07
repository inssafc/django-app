from django.conf import settings
from .models import Cart, CartItem, Product

def get_or_create_cart(request):
    if request.user.is_authenticated:
        session_id = request.session.session_key
        if session_id:
            try:
                session_cart = Cart.objects.get(session_id=session_id, user__isnull=True)
                # Associer ce panier à l'utilisateur maintenant connecté
                session_cart.user = request.user
                session_cart.save()
                return session_cart
            except Cart.DoesNotExist:
                pass
        
        cart, created = Cart.objects.get_or_create(user=request.user, defaults={'session_id': None})
        return cart
    else:
        session_id = request.session.session_key
        if not session_id:
            request.session.create()
            session_id = request.session.session_key
        
        cart, created = Cart.objects.get_or_create(session_id=session_id, defaults={'user': None})
        return cart

def add_to_cart(request, product_id, quantity=1):
    cart = get_or_create_cart(request)
    product = Product.objects.get(id=product_id)
    
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity += quantity
        cart_item.save()
    except CartItem.DoesNotExist:
        CartItem.objects.create(cart=cart, product=product, quantity=quantity)
    
    return cart

def remove_from_cart(request, product_id):
    cart = get_or_create_cart(request)
    product = Product.objects.get(id=product_id)
    
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except CartItem.DoesNotExist:
        pass
    
    return cart

def clear_cart(request):
    cart = get_or_create_cart(request)
    cart.items.all().delete()
    return cart

def get_cart_items(request):
    cart = get_or_create_cart(request)
    return cart.items.all()

def get_cart_total(request):
    cart = get_or_create_cart(request)
    return cart.get_total_price()