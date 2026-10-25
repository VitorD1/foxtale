from django.urls import path

from products.views import (
    CategoryCreateView,
    CategoryListView,
    OccasionCreateView,
    OccasionListView,
    ProductCreateView,
    ProductListView,
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('add/', ProductCreateView.as_view(), name='product-add'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/add/', CategoryCreateView.as_view(), name='category-add'),
    path('occasions/', OccasionListView.as_view(), name='occasion-list'),
    path('occasions/add/', OccasionCreateView.as_view(), name='occasion-add'),
]