from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from client.forms import ClientForm
from client.models import Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Создание клиента"
        return context

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientListView(ListView):
    model = Client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Список клиентов сервера"
        return context


class ClientDetailView(DetailView):
    model = Client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Подробная информация о пользователе"
        return context


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse('client:view', args=[self.kwargs.get('pk')])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client:list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object