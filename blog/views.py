from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.forms import BlogForm
from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    # success_url = reverse_lazy('blog:list')


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm


class BlogDeleteView(DeleteView):
    model = Blog
