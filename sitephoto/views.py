from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from .models import Blog, Photo, About, Connection, PhotoCollect


class BaseView(View):
    '''Стартовая страница'''

    def get(self, request):
        return render(request, 'base.html')


class PhotoList(ListView):
    '''Страница представления фото коллекции'''
    paginate_by = 2
    model = Photo
    template_name = 'photo/photo_list_view.html'
    context_object_name = 'photos'


class PhotoDetail(DetailView, MultipleObjectMixin):
    '''Раздел по фото коллекции'''
    paginate_by = 2
    model = Photo
    template_name = 'photo/photo_detail.html'
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        object_list = PhotoCollect.objects.filter(movie=self.get_object())
        context = super(PhotoDetail, self).get_context_data(object_list=object_list, **kwargs)
        return context


class BlogList(ListView):
    '''Страница блога с фото'''
    paginate_by = 1
    model = Blog
    template_name = 'blog/blog_list_view.html'
    context_object_name = 'blogs'


class BlogDetail(DetailView):
    '''Раздел по блогу'''
    model = Blog
    template_name = 'blog/blog_detail_view.html'
    context_object_name = 'blog'


class AboutView(View):
    '''Страница о нас'''

    def get(self, request):
        about = About.objects.all()
        return render(request, 'about/about_view.html', context={'about': about})


class ConnectionCreate(CreateView):
    '''Для обратной связи'''
    model = Connection
    template_name = 'connect/connection.html'
    fields = ['name', 'email', 'text']
    success_url = '/connection/'


class ConnectionUpdate(UpdateView):
    '''обновление'''
    model = Connection
    template_name = 'connect/connection.html'
    fields = ['name', 'email', 'text']
    success_url = '/connection/'


class ConnectionDelete(DeleteView):
    '''удаление'''
    model = Connection
    template_name = 'connect/connection.html'
    fields = ['name', 'email', 'text']
    success_url = reverse_lazy('base_view')
