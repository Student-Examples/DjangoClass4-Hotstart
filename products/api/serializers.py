from rest_framework.serializers import ModelSerializer

from products.models import Category, Product


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description", "is_active", "created_date"]


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "count", "created_date"]