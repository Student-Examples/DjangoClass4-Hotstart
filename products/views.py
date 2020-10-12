from django.views.generic import TemplateView

from products.models import Product


class ProductListView(TemplateView):
    template_name = "product_list.html"

    def get_context_data(self, **kwargs):
        products = Product.objects.all()
        return {
            "products": products
        }
