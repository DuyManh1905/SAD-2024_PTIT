from django.urls import path, re_path
from . import views
from django.views.static import serve

urlpatterns = [
    # other commented code here
    path('', views.home, name='home'),
]