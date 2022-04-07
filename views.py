from django.shortcuts import render
from .models import Post, Category, Author
from django.views.generic import DetailView
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, DetailView,DeleteView
from django.core.paginator import Paginator
from .filters import PostFilter
from .forms import PostForm


class news(ListView):
    model = Post
    template_name = 'news_portal/news.html'
    context_object_name = 'news'
    ordering = ['dateCreation']
    paginate_by = 1  # поставим постраничный вывод в один элемент

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'news_portal/details_view.html'
    queryset = Post.objects.all()


class PostCreateView(CreateView):
    template_name = 'news_portal/news_create.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    template_name = 'news_portal/news_create.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class PostDeleteView(DeleteView):
    template_name = 'news_portal/news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


def about(request):
    return render(request, 'news_portal/about.html')