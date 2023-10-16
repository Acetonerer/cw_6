from django.contrib import admin

from client.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    search_fields = ('email',)
