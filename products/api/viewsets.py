from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from products.api.permissions import MyTokenPermission
from products.api.serializers import CategorySerializer, ProductSerializer
from products.models import Category


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [MyTokenPermission]

    @action(methods=["get"], detail=True, url_path="products")
    def get_products(self, request, pk):
        category = self.get_object()
        products = category.products.all()
        serializer = ProductSerializer(products, many=True)

        print(request.user)

        return Response(data=serializer.data)
