from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from products.api.drf_views import CategoriesListApiView, CategoryDetailsApiView, ProductsListApiView, \
    ProductDetailsApiView, ProductsListByCategoryApiView

urlpatterns = [
    path("categories/", csrf_exempt(CategoriesListApiView.as_view())),
    path("categories/<int:name>/", csrf_exempt(CategoryDetailsApiView.as_view())),

    path("products/", csrf_exempt(ProductsListApiView.as_view())),
    path("categories/<int:id>/products/", csrf_exempt(ProductsListByCategoryApiView.as_view())),
    path("products/<int:id>/", csrf_exempt(ProductDetailsApiView.as_view())),
]
