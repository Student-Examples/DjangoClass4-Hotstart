import json

from django.http import JsonResponse
from django.views import View

from products.api.serializers import CategorySerializer
from products.models import Category


class CategoriesListApiView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"status": "SUCCESS"}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

class CategoryDetailsApiView(View):
    def get(self, request, *args, **kwargs):
        try:
            category_id = kwargs["id"]
            category = Category.objects.get(id=category_id)
        except:
            return JsonResponse({"status": "ERROR", "message": "Not found"}, status=404)

        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data)

    def delete(self, request, *args, **kwargs):
        try:
            category_id = kwargs["id"]
            category = Category.objects.get(id=category_id)
        except:
            return JsonResponse({"status": "ERROR", "message": "Not found"}, status=404)

        category.delete()
        return JsonResponse({"status": "SUCCESS"})

