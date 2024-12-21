from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product

@api_view(http_method_names=['GET'])
def product_list_api_view(request):
# Step 1: Collect all products from DB - DataBase (QuerySet)
    products = Product.objects.all()
# Step 2: Reformat (Serialize) data to list of Dictionary
    list_ = []
    for product in products:
        list_.append(
            model_to_dict(product)
        )
# Step 3: Return  response with data and status (default: 200)
    return Response(data=list_, status=status.HTTP_200_OK)