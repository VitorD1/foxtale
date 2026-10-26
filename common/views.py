from django.views.generic import TemplateView

from products.models import Product
from stories.models import Article


class HomeView(TemplateView):
    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()[:5]
        context['articles'] = Article.objects.all()[:5]
        return context