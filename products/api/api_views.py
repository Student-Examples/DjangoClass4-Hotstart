from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.mixins import DestroyModelMixin

from products.api.serializers import CategorySerializer, ProductSerializer
from products.models import Category, Product


class CategoriesListApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveDestroyView(RetrieveAPIView, DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def delete(self, request, *arg, **kwargs):
        return self.destroy(request, *arg, **kwargs)


class ProductListApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
