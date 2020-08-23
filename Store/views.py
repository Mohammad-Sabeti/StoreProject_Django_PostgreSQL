from django.shortcuts import render
from .models import Product,OrderApp,Customer
# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/product_list.html', context)