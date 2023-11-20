from django.shortcuts import render
from .models import User, Product
# Create your views here.

def product_list(request): 
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})


