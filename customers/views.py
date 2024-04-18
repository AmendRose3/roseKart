from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages  # Import messages module
from .models import Customer

def show_account(request):
    if request.POST and 'register' in request.POST:
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            
            # Create user accounts
            user = User.objects.create(
                username=username,
                password=password,
                email=email
            )
            # Create customer account
            customer = Customer.objects.create(   
                user=user,
                phone=phone,
                address=address
            )
            return redirect('home')
        except Exception as e:
            error_message = "Duplicate username or invalid credentials"
            messages.error(request, error_message)
    return render(request, 'account.html')
