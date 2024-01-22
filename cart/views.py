from django.shortcuts import render
from . import views
from cart import cart


# Create your views here.
def show_cart(request, template_name="cart/cart.html"):
    cart_items = cart.get_cart_items(request)
    print('cart_items', cart_items)
    page_title = "Shopping Cart"
    cart_subtotal = cart.cart_subtotal(request)
    print('subtotal', cart_subtotal)
    cart_item_count = len(cart_items)
    return render(request, template_name,  locals(),)