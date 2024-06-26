"""
URL configuration for onlineshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('store.urls')),
# ]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('store.urls')),  # Include store app URLs

#     # Authentication URLs
#     path('accounts/', include('django.contrib.auth.urls')),  # Django auth URLs

# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# onlineshop/urls.py

from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views  # Import auth views for login/logout
from store import views
from store.views import YourRegisterView  # Import YourRegisterView from your views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URLs
    path('', include('store.urls')),  # Include app-specific URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in authentication URLs
    path('accounts/register/', YourRegisterView.as_view(), name='register'),  # Custom register view
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Built-in login view
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Built-in logout view
    path('item/<int:item_id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
]

