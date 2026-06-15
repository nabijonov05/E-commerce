from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from apps.products.api_endpoints.categories.CategoryList.serializers import CategoryListSerializer
from apps.products.models import Category


# @api_view(['GET'])
# def category_list(request):
#     categories = Category.objects.all()
#     serializer = CategoryListSerializer(categories, many=True)
#     return Response(serializer.data)

class CategorCreateAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer