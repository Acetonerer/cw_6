from django.urls import path
from django.views.decorators.cache import cache_page

from mailling.apps import MaillingConfig
from mailling.views import MessageCreateView, MessageDeleteView, \
    MessageUpdateView, LogsListView, MaillingCreateView, MaillingListView, MaillingDetailView, MaillingUpdateView, \
    MaillingDeleteView, MainView

app_name = MaillingConfig.name


urlpatterns = [
    path('create/', MessageCreateView.as_view(), name='create'),
    path('logs/list/', LogsListView.as_view(), name='logs_list'),
    path('mailling/list/', cache_page(60)(MaillingListView.as_view()), name='mailling_list'),
    path('', MainView.as_view(), name='list'),
    path('edit/<int:pk>/', MessageUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', MessageDeleteView.as_view(), name='delete'),
    path('mailling/create/', MaillingCreateView.as_view(), name='mailling_create'),
    path('mailling/view/<int:pk>/', MaillingDetailView.as_view(), name='mailling_view'),
    path('mailling/edit/<int:pk>/', MaillingUpdateView.as_view(), name='mailling_edit'),
    path('mailling/delete/<int:pk>/', MaillingDeleteView.as_view(), name='mailling_delete'),
]
