from rest_framework.serializers import ModelSerializer

from products.models import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description", "is_active", "created_date"]
