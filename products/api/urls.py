from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter

from products.api.api_views import CategoriesListApiView, ProductListApiView, CategoryRetrieveDestroyView
from products.api.viewsets import CategoryViewSet

router = DefaultRouter()
router.register("cats", CategoryViewSet)


urlpatterns = [
    path("", include(router.urls)),

    path("categories/", csrf_exempt(CategoriesListApiView.as_view())),
    path("categories/<pk>/", csrf_exempt(CategoryRetrieveDestroyView.as_view())),
    path("products/", csrf_exempt(ProductListApiView.as_view())),
    # path("categories/<int:id>/products/", csrf_exempt(ProductsListByCategoryApiView.as_view())),
    # path("products/<int:id>/", csrf_exempt(ProductDetailsApiView.as_view())),
]
