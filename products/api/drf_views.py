import json

from django.http import JsonResponse
from django.views import View

from products.api.serializers import CategorySerializer, ProductSerializer
from products.models import Category, Product


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


class ProductsListApiView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


class ProductsListByCategoryApiView(View):
    def get(self, request, *args, **kwargs):
        try:
            category = Category.objects.get(id=kwargs["id"])
        except:
            return JsonResponse({"status": "ERROR", "message": "Category ot found"}, status=404)
        serializer = ProductSerializer(category.products.all(), many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        try:
            category = Category.objects.get(id=kwargs["id"])
        except:
            return JsonResponse({"status": "ERROR", "message": "Category ot found"}, status=404)
        data = json.loads(request.body)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save(category=category)
            return JsonResponse({"status": "SUCCESS"}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)


class ProductDetailsApiView(View):
    def get(self, request, *args, **kwargs):
        try:
            product_id = kwargs["id"]
            product = Product.objects.get(id=product_id)
        except:
            return JsonResponse({"status": "ERROR", "message": "Not found"}, status=404)

        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)

    def delete(self, request, *args, **kwargs):
        try:
            product_id = kwargs["id"]
            product = Product.objects.get(id=product_id)
        except:
            return JsonResponse({"status": "ERROR", "message": "Not found"}, status=404)

        product.delete()
        return JsonResponse({"status": "SUCCESS"})

