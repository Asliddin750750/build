from django.urls import path

from api.views import BrandsView, BrandCreateView, ProductsView

urlpatterns = [
    path('brands/', BrandsView.as_view(), name='brands'),
    path('brand/create/', BrandCreateView.as_view(), name='brand-create'),
    path('products/', ProductsView.as_view(), name='products')
]
