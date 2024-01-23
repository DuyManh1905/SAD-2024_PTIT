from django.shortcuts import render
from django.template import RequestContext
from cart import cart


def show_cart(request, template_name="cart/cart.html"):
    if request.method == 'POST':
        postdata = request.POST.copy()

        if postdata.get('submit') == 'Remove':
            cart.remove_from_cart(request)

        if postdata.get('submit') == 'Update':
            cart.update_cart(request)

    cart_items = cart.get_cart_items(request)
    page_title = 'Shopping Cart'
    cart_subtotal = cart.cart_subtotal(request)

    return render(request, template_name, {'cart_items': cart_items, 'page_title': page_title,
                                            'cart_subtotal': cart_subtotal})
