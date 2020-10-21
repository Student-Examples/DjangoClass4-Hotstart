from rest_framework.fields import SerializerMethodField
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from products.models import Category, Product


class ProductSerializer(ModelSerializer):
    category = StringRelatedField(read_only=True)
    # category = CategorySerializer()

    class Meta:
        model = Product
        fields = ["id", "name", "price", "count", "created_date", "category"]


class CategorySerializer(ModelSerializer):
    short_name = SerializerMethodField()
    human_date = SerializerMethodField()
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        depth = 1
        fields = ["id", "name", "description", "is_active", "created_date", "short_name",
                  "human_date", "products"]

    def get_short_name(self, category):
        return category.name[:5]

    def get_human_date(self, category):
        return category.created_date.strftime("%d %B")
