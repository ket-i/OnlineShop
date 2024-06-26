from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Category, Brand, Item, Review, Cart, CartItem
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import ReviewForm

def product_list(request):
    items = Item.objects.all()  # Updated to Item
    categories = Category.objects.all()
    brands = Brand.objects.all()
    category_id = request.GET.get('category')
    brand_id = request.GET.get('brand')
    if category_id:
        items = items.filter(category_id=category_id)
    if brand_id:
        items = items.filter(brand_id=brand_id)
    return render(request, 'product_list.html', {'items': items, 'categories': categories, 'brands': brands}) 

def product_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    reviews = Review.objects.filter(item=item)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.item = item
            new_review.user = request.user  # Assuming Review model has a 'user' field
            new_review.save()
            return redirect('product_detail', item_id=item_id)

    else:
        review_form = ReviewForm()

    return render(request, 'product_detail.html', {'item': item, 'reviews': reviews, 'review_form': review_form})

@login_required
def add_to_cart(request, item_id):  # Updated to Item
    item = get_object_or_404(Item, id=item_id)  # Updated to Item
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)  # Updated to Item
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'cart_detail.html', {'cart': cart})

@login_required
def remove_from_cart(request, item_id):  # Updated to Item
    cart = get_object_or_404(Cart, user=request.user)
    item = get_object_or_404(Item, id=item_id)  # Updated to Item
    cart_item = get_object_or_404(CartItem, cart=cart, item=item)  # Updated to Item
    cart_item.delete()
    return redirect('cart_view')

def cart_detail(request):
    user = request.user
    cart = get_object_or_404(Cart, user=user)
    return render(request, 'cart_detail.html', {'cart': cart})

def cart_detail(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    return render(request, 'store/cart_detail.html', {'cart': cart})

def add_to_cart(request, item_id):
    item = Item.objects.get(id=item_id)
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(reverse('cart_detail'))  

class YourRegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  
    template_name = 'registration/register.html'  

def product_list(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    items = Item.objects.all()
    
    category_id = request.GET.get('category')
    brand_id = request.GET.get('brand')
    
    if category_id:
        items = items.filter(category_id=category_id)
    if brand_id:
        items = items.filter(brand_id=brand_id)

    return render(request, 'store/product_list.html', {
        'items': items,
        'categories': categories,
        'brands': brands,
    })


