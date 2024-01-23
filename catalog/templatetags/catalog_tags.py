from django import template 
from cart import cart 
from catalog.models import Category


register = template.Library() 


@register.inclusion_tag("tags/cart_box.html") 
def cart_box(request): 
 cart_item_count = cart.cart_distinct_item_count(request) 
 return {'cart_item_count': cart_item_count } 


@register.inclusion_tag("tags/category_list.html") 
def category_list(request_path):
    active_category = Category.objects.filter(is_active=True)
    return {
        'active_category': active_category,
        'request_path': request_path
    }
