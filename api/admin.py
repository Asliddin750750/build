from django.contrib import admin

from api.models import Product, Brand

admin.site.register(Brand)
admin.site.register(Product)