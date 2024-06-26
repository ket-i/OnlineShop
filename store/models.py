from django.db import models

from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField(max_length=1024)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    brand = models.ForeignKey(Brand, related_name='items', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    stock = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    details = models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    rating = models.IntegerField()
    comment = models.TextField()
   

    def __str__(self):
        return f'Review by {self.user.username} for {self.item.name}'

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    items = models.ManyToManyField(Item, through='CartItem')

    def total_price(self):
        return sum(item.total_price() for item in self.cartitem_set.all())

class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.item.price * self.quantity
    

        



