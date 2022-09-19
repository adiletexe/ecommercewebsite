from django.shortcuts import render
from django.http import HttpResponse
from .models import Cart, CartItem
from store.models import Product
# Create your views here.
def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.get(cart=cart, is_available=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.product.quantity)
            quantity += cart_item.quantity


    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
    }
    return render(request, 'cart/cart.html', context)

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()

    return render(request, 'cart/cart.html')

