from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.views.generic.edit import CreateView


# Create your views here.
def home(request):
    products =Product.objects.all()
    category = Category.objects.all()
    context = {
        'products':products,
        'categorys':category,
    }
    return render(request, 'store/home.html', context)


@login_required
def homev(request):
    products = Product.objects.all()
    category = Category.objects.all()
    context = {
        'products':products,
        'categorys':category,
    }
    return render(request, 'store/homev.html', context)


@login_required
def vendorCreateProduct(request):
    form = CreateProduct(request.POST)
    if request.method == 'POST':
        form = CreateProduct(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.product_vendor = request.user
            product.save()
            messages.success(request, "Product Created", fail_silently=True)
            return redirect('homev')
        else:
            messages.error(request, "Error")
            form.errors
    context = {
        'forms': form
    }
    return render(request, 'store/create-product.html', context)

