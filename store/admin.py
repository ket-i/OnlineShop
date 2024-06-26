# from django.contrib import admin
# from .models import Item, Review, Category, Brand

# admin.site.register(Item)

# admin.site.register(Review)

# admin.site.register(Category)
# admin.site.register(Brand)


from django.contrib import admin
from .models import Category, Brand, Item, Review, Cart, CartItem

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Item)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(CartItem)
