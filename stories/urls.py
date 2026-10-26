from django.urls import path

from stories.views import (
    ArticleCreateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleEditView,
    ArticleListView,
    SectionView,
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('add/', ArticleCreateView.as_view(), name='article-add'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:pk>/edit/', ArticleEditView.as_view(), name='article-edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('section/<str:section>/', SectionView.as_view(), name='section'),
]