from rest_framework import serializers

from api.models import Product


class ProductsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('brand', 'image')

    def get_image(self, obj):
        request = self.context.get('request')
        print(request)
        image_url = obj.image.url
        if request:
            return request.build_absolute_uri(image_url)
        else:
            return image_url
