from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from products.forms import CategoryForm, OccasionForm, ProductForm
from products.models import Category, Occasion, Product


class CategoryListView(ListView):
    model = Category
    template_name = 'products/category_list.html'

    def get_queryset(self):
        return Category.objects.annotate(total=Count('products'))


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'products/category_form.html'
    success_url = reverse_lazy('category-list')


class OccasionListView(ListView):
    model = Occasion
    template_name = 'products/occasion_list.html'

    def get_queryset(self):
        return Occasion.objects.annotate(total=Count('products'))


class OccasionCreateView(CreateView):
    model = Occasion
    form_class = OccasionForm
    template_name = 'products/occasion_form.html'
    success_url = reverse_lazy('occasion-list')


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product-list')