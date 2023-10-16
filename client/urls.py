from django.urls import path, include

from client.apps import ClientConfig
from client.views import ClientCreateView, ClientListView, ClientDetailView, ClientUpdateView, ClientDeleteView

app_name = ClientConfig.name
urlpatterns = [
    path('create/', ClientCreateView.as_view(), name='create'),
    path('', ClientListView.as_view(), name='list'),
    path('view/<int:pk>/', ClientDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', ClientUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ClientDeleteView.as_view(), name='delete'),
]
