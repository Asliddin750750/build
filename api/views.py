from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Product
from api.serializers import ProductsSerializer


class BrandsView(APIView):
    def get(self, request):
        return Response({
            'success': True,
            'data': 'data'
        }, status=status.HTTP_200_OK)


class BrandCreateView(APIView):
    def post(self, request):
        return Response({
            'success': True,
            'data': 'data'
        }, status=status.HTTP_200_OK)


class ProductsView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductsSerializer(queryset, many=True, context={'request': request})
        return Response({
            'success': True,
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        Product(brand_id=request.data.get('brand'), image=request.data.get('image')).save()
        return Response({
            'success': True,
            'data': "AAA"
        }, status=status.HTTP_200_OK)
