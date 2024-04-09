from django.shortcuts import render
from . models import Product

# View function for the homepage
def index(request):
    return render(request, 'index.html')

# View function for the product list page
def list_products(request):
    # Logic to fetch and display product list
    product_list=Product.object.all()
    context={'products':product_list}
    return render(request, 'products.html')

# View function for the product detail page
def detail_product(request):
    # Logic to fetch and display product details
    return render(request, 'product_detail.html')
