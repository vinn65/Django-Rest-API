from django.http import JsonResponse
from django.forms import model_to_dict
import json
from products.models import Product


def api_home(request,*args,**kwargs):
     model_data = Product.objects.all().order_by("?").first()
     data = {}
     if model_data:
          data = model_to_dict(model_data)# can add specific fields using fields= ["field1"]
          """
          the process below is complex .
          model instance, turn it into python dict and return json to client
          use the above instead
          """
        #   data['id'] = model_data.id
        #   data['title'] = model_data.title
        #   data['content'] = model_data.content
        #   data['price'] = model_data.price
     return JsonResponse(data)


# def api_home(request,*args,**kwargs):

#     body = request.body
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     print(data.keys)
#     return JsonResponse({"message":"Hello this is your Django API response"})
