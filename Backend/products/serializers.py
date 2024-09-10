from rest_framework import serializers
from . models import Product
from rest_framework.reverse import reverse

class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = "product-detail",
        lookup_field = 'pk'
    )
    class Meta:
        model = Product
        fields = [
            'url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price'
        ]
    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", kwargs = {'pk':obj.pk}, request= request)
