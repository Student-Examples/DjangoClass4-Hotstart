from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from products.api.views import CategoriesListApiView, CategoryDetailsApiView

urlpatterns = [
    path("categories/", CategoriesListApiView.as_view()),
    path("categories/<int:id>/", csrf_exempt(CategoryDetailsApiView.as_view())),
]