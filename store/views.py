from django.shortcuts import render


# Create your views here.

def home(request):

	return render(request, 'store/home-page.html', {})

def checkout(request):

	return render(request, 'store/checkout-page.html', {})

def product(request):

	return render(request, 'store/product-page.html', {})