# from django.http import JsonResponse
from django.forms import model_to_dict
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer
from rest_framework import status


@api_view(["GET","POST"])
def api_home(request,*args,**kwargs):
     if request.method == "POST":
          serializer = ProductSerializer(data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
     instance = Product.objects.all().order_by("?").first()
     data = {}
     if instance:
        #   data = model_to_dict(instance)# can add specific fields using fields= ["field1"]
          data = ProductSerializer(instance).data
          """
          the process below is complex .
          model instance, turn it into python dict and return json to client
          use the above instead
          """
        #   data['id'] = instance.id
        #   data['title'] = model_data.title
        #   data['content'] = model_data.content
        #   data['price'] = model_data.price
     return Response(data)


# def api_home(request,*args,**kwargs):

#     body = request.body
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     print(data.keys)
#     return JsonResponse({"message":"Hello this is your Django API response"})
