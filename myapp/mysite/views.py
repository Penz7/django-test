from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ProductForm

def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('/dashboard')

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
          
            user_obj = authenticate(request, username=username, password=password)

            if user_obj and user_obj.is_superuser:
                login(request, user_obj)
                return redirect('/dashboard/')
            else:
                messages.error(request, 'Invalid username or password')

        return render(request, 'login.html')

    except Exception as e:
        print(e)


def product_list(request): 
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})


def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ProductForm(instance=product)

    return render(request, 'dashboard.html', {'form': form, 'product': product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'DELETE':
        product.delete()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
    
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')