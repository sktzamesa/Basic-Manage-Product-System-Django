# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from products.views import admin_view  # Ensure this path is correct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admin_view, name='home'),  # Map the root URL to the admin_view
    path('products/', include('products.urls')),  # Include URLs from the products app
]
