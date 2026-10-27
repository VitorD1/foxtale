from django import template

from products.models import Product

register = template.Library()

@register.filter
def reading_time(text):
    return len(text.split()) // 200 + 1

@register.simple_tag
def products_count():
    return Product.objects.count()