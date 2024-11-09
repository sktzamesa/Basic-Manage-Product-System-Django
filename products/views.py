# products/views.py

from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def admin_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_view')
    else:
        form = ProductForm()
    products = Product.objects.all()
    return render(request, 'admin_page.html', {'form': form, 'products': products})
