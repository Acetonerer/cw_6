from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail
from django.utils import timezone

from client.models import Client
# from config import settings
from mailling.models import Mailling


def send_message_email(mailling_item: Mailling):
    now = timezone.localtime(timezone.now())

    recepients = [client.email for client in mailling_item.client.all()]
    if mailling_item.date_start <= now <= mailling_item.date_end:
        send_mail(
         f"{mailling_item.message.subject_letter}",
         f"{mailling_item.message.body_letter}",
         settings.EMAIL_HOST_USER,
         recepients
        )
        mailling_item.status = 'started'
        mailling_item.save()


def get_cache_count_mailling():
    if settings.CACHE_ENABLED:
        key = 'mailling'
        mailling = cache.get(key)
        if mailling is None:
            mailling = Mailling.objects.all().count()
            cache.set(key, mailling)
    else:
        mailling = Mailling.objects.all().count()
    return mailling


def get_cache_count_client():
    if settings.CACHE_ENABLED:
        key = 'client'
        client = cache.get(key)
        if client is None:
            client = Client.objects.all().count()
            cache.set(key, client)
    else:
        client = Client.objects.all().count()
    return client
