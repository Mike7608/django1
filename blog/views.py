from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.utils.text import slugify

from blog.forms import BlogForm, VersionForm
from blog.models import Blog, Version


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
    # fields = ("heading", 'text', "pict")
    form_class = BlogForm
    # success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        new_blog = form.save(commit=False)
        new_blog.slug = slugify(new_blog.heading)
        new_blog.save()
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')


class BlogUpdateView(UpdateView):
    model = Blog
    # fields = ("heading", 'text', "pict")
    form_class = BlogForm
    # success_url = reverse_lazy('blog:blog_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Blog, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


def publish(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)

    if blog_item.published:
        blog_item.published = False
    else:
        blog_item.published = True

    blog_item.save()
    return redirect(reverse('blog:list'))

