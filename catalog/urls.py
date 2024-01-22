from django.urls import path
from .views import index, show_category, show_product
from . import views

urlpatterns = [
    path('', views.index, {'template_name': 'catalog/index.html'}, name='catalog_home'),
    path('index/', views.index, {'template_name': 'catalog/index.html'}, name='catalog_home'),
    path('category/<slug:category_slug>/', views.show_category, {'template_name': 'catalog/category.html'}, name='catalog_category'),
    path('product/<slug:product_slug>/', views.show_product, {'template_name': 'catalog/product.html'}, name='catalog_product'),
]
