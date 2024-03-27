from django.shortcuts import render

# View function for the homepage
def index(request):
    return render(request, 'index.html')

# View function for the product list page
def list_products(request):
    # Logic to fetch and display product list
    return render(request, 'products.html')

# View function for the product detail page
def detail_product(request):
    # Logic to fetch and display product details
    return render(request, 'product_detail.html')
