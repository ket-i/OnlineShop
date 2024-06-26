# # store/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('login/', views.user_login, name='user_login'),
#     path('logout/', views.user_logout, name='user_logout'),
#     path('register/', views.user_register, name='user_register'),
#     path('', views.item_list, name='item_list'),
#     path('item/<int:item_id>/', views.item_detail, name='item_detail'),
#     path('cart/', views.cart, name='cart'),
#     path('item/<int:item_id>/add_review/', views.add_review, name='add_review'),
#     path('cart/add/<int:item_id>/', views.add_item_to_cart, name='add_to_cart'),
#     path('cart/remove/<int:item_id>/', views.remove_item_from_cart, name='remove_item_from_cart'),
#]

# from django.urls import path
# from django.contrib.auth import views as auth_views
# from . import views

# urlpatterns = [
#     path('', views.item_list, name='item_list'),
#     path('item/<int:item_id>/', views.item_detail, name='item_detail'),
#     path('item/<int:item_id>/add_review/', views.add_review, name='add_review'),
#     path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
#     path('cart/', views.cart_view, name='cart_view'),
#     path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    
#     # Authentication URLs
#     path('login/', auth_views.LoginView.as_view(template_name='store/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('register/', views.register, name='register'),  # Create a view for registration
#     # Add more authentication-related URLs as needed
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('item/<int:item_id>/', views.product_detail, name='product_detail'),  # Updated to Item
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),  # Updated to Item
    path('cart/', views.cart_detail, name='cart_view'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),  # Updated to Item
]






# urlpatterns = [
#     path('', views.index, name='index'),
#     path('item/<int:item_id>/', views.item_detail, name='item_detail'),
#     path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
#     path('cart/', views.cart_detail, name='cart_detail'),
#     path('update_cart_item/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
#     path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
#     path('search/', views.search, name='search'),
#     path('update_product_rating/<int:item_id>/', views.update_product_rating, name='update_product_rating'),
# ]


