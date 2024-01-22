from django.urls import path, include
from . import views
from .views import show_cart

urlpatterns = [
    path("", views.show_cart, {'template_name': 'cart/cart.html'}, name="show_cart",),
]