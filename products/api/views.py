import json

from django.http import JsonResponse
from django.views import View

from products.models import Category


class CategoriesListApiView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()

        categories_data = []
        for category in categories:
            category_data = {
                "id": category.id,
                "name": category.name,
                "description": category.description,
                "is_active": category.is_active,
                "created_date": category.created_date.strftime("%d.%m.%Y %H:%M")
            }
            categories_data.append(category_data)

        return JsonResponse(categories_data, safe=False)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            Category.objects.create(name=data["name"], description=data["description"])
        except KeyError:
            return JsonResponse({"status": "ERROR", "message": "name and desc required"}, status=400)

        return JsonResponse({"status": "SUCCESS"}, status=201)


class CategoryDetailsApiView(View):
    def get(self, request, *args, **kwargs):
        try:
            category_id = kwargs["id"]
            category = Category.objects.get(id=category_id)
        except:
            return JsonResponse({"status": "ERROR", "message": "Not found"}, status=404)

        category_data = {
            "id": category.id,
            "name": category.name,
            "description": category.description,
            "is_active": category.is_active,
            "created_date": category.created_date.strftime("%d.%m.%Y %H:%M")
        }
        return JsonResponse(category_data)

    def delete(self, request, *args, **kwargs):
        try:
            category_id = kwargs["id"]
            category = Category.objects.get(id=category_id)
        except:
            return JsonResponse({"status": "ERROR", "message": "Not found"}, status=404)

        category.delete()
        return JsonResponse({"status": "SUCCESS"})

