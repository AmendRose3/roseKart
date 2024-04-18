# products/views.py
from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# View function for the homepage
# View function for the homepage
def index(request):
    featured_products = Product.objects.order_by('-priority')[:4]
    latest_products = Product.objects.order_by('-id')[4:8]
    context = {
        'featured_products': featured_products,
        'latest_products': latest_products
    }
    print(context)
    return render(request, 'index.html', context)


# View function for the product list page
def list_products(request):
    # Logic to fetch and display product list
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=Product.objects.order_by('-priority')
    product_paginator=Paginator(product_list,2)
    product_list=product_paginator.get_page(page)
    context={'products':product_list}
    return render(request,'products.html',context)


# View function for the product detail page
def detail_product(request,pk):
    product=Product.objects.get(pk=pk)
    context={'product':product}
    return render(request,'product_detail.html',context)


