from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from pytils.translit import slugify

from blog.models import Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.total_view += 1
        self.object.save()
        return self.object


class BlogListView(ListView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ("heading", 'text', "pict", 'published')
    # success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.heading)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        # ВОТ ЗДЕСЬ ПРОБЛЕМА!!!!!
        # НЕ ПЕРЕХОДИТ В ПРОСМОТР
        return reverse('blog:blog_view', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("heading", 'text', "pict", 'published')
    success_url = reverse_lazy('blog:blog_list')


def publish(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)

    if blog_item.published:
        blog_item.published = False
    else:
        blog_item.published = True

    blog_item.save()
    return redirect(reverse('blog:blog_list'))
