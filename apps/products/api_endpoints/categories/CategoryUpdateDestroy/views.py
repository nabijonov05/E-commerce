from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.products.api_endpoints.categories.CategoryUpdateDestroy.serializers import CategoryUpdateDestroySerializer
from apps.products.models import Category


@api_view(['PATCH', 'DELETE'])
def category_update_destroy(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=404)

    if request.method == 'PATCH':
        serializer = CategoryUpdateDestroySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            category = serializer.save()
            return Response(CategoryUpdateDestroySerializer(category).data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=204)
