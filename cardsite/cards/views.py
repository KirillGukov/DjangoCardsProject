from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from .forms import AddPostForm, UploadFilesForm
from .models import Posts, Category, TagPost, UploadFiles
from .utils import DataMixin


class CardsHome(DataMixin, ListView):
    template_name = 'cards/index.html'
    context_object_name = 'posts'
    title_page = 'Dream House'
    cat_selected = 0


    def get_queryset(self):
        return Posts.published.all().select_related('cat')


def load_image(request):
    contact_list = Posts.published.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'cards/load_image.html',
                  {'title': 'Изображение', 'page_obj': page_obj})



class ShowPost(DataMixin ,DetailView):
    template_name = 'cards/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)


    def get_object(self, queryset=None):
        return get_object_or_404(Posts.published, slug=self.kwargs[self.slug_url_kwarg])


class AddPost(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'cards/add_post.html'
    title_page = 'Добавление статьи'
    success_url = reverse_lazy('home')


class UpdatePost(DataMixin, UpdateView):
    model = Posts
    fields = ['title', 'content', 'images', 'is_published', 'cat']
    template_name = 'cards/add_post.html'
    success_url = reverse_lazy('home')
    title_page = 'Редактирование статьи'


class DeletePost(DeleteView):
    model = Posts
    template_name = 'cards/add_post.html'
    success_url = reverse_lazy('home')



def contacts(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


class PostsCategory(DataMixin, ListView):
    template_name = 'cards/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Posts.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        return self.get_mixin_context(context,
                                      title='Категория - ' + cat.name,
                                      cat_selected=cat.pk
                                      )


class TagPostList(DataMixin, ListView):
    template_name = 'cards/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        return self.get_mixin_context(context, title='Тег: ' + tag.tag)


    def get_queryset(self):
        return Posts.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

