

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('item/<int:item_id>/', views.product_detail, name='product_detail'),  # Updated to Item
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),  # Updated to Item
    path('cart/', views.cart_detail, name='cart_view'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),  # Updated to Item
]







