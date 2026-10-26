
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from stories.forms import ArticleEditForm, ArticleForm
from stories.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'stories/article_list.html'


class SectionView(ListView):
    model = Article
    template_name = 'stories/section.html'

    def get_queryset(self):
        section = self.kwargs['section']
        if section not in Article.Section.values:
            raise Http404
        return Article.objects.filter(section=section)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Article.Section(self.kwargs['section']).label
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'stories/article_detail.html'


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'stories/article_form.html'
    success_url = reverse_lazy('article-list')


class ArticleEditView(UpdateView):
    model = Article
    form_class = ArticleEditForm
    template_name = 'stories/article_edit.html'
    success_url = reverse_lazy('article-list')


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'stories/article_delete.html'
    success_url = reverse_lazy('article-list')
