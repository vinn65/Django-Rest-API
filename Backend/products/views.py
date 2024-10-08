from rest_framework import generics, mixins
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Product
from . serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from api.mixins import StaffEditorPermissionMixin


class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    

product_list_create_view = ProductListCreateAPIView.as_view()
class ProductDetailAPIView(StaffEditorPermissionMixin, 
                           generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(StaffEditorPermissionMixin,
                           generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(StaffEditorPermissionMixin,
                            generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()


class ProductListAPIView(StaffEditorPermissionMixin,
                         generics.ListAPIView):

    query_set = Product.objects.all()
    serializer_class = ProductSerializer

product_list_view = ProductListAPIView.as_view()


# class ProductMixinView(generics.GenericAPIView):

#     def get  



@api_view(["GET","POST"])
def product_alt_view(request, pk= None, *args, **kwargs):
    method = request.method
    if method == "GET":
        if pk  is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj).data

            return Response(data)
        
        query_set = Product.objects.all()
        data = ProductSerializer(query_set, many=True).data
        return Response(data)
    if method == "POST":
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data

    return Response(data)
