from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from products.forms import CategoryForm, OccasionForm, ProductEditForm, ProductFilterForm, ProductForm
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

    def get_queryset(self):
        products = Product.objects.all()
        form = ProductFilterForm(self.request.GET)

        if form.is_valid():
            category = form.cleaned_data['category']
            occasion = form.cleaned_data['occasion']
            sort = form.cleaned_data['sort']

            if category:
                products = products.filter(category=category)
            if occasion:
                products = products.filter(occasions=occasion)
            if sort:
                products = products.order_by(sort)

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = ProductFilterForm(self.request.GET)
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product-list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


class ProductEditView(UpdateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'products/product_edit.html'
    success_url = reverse_lazy('product-list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('product-list')
