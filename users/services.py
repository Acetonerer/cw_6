from django.core.mail import send_mail

from config import settings


def send_verif_code(user, url):
    send_mail(
        'Подтверждение регистрации',
        f'Для подтверждения регистрации пользователя {user.email} пройдите по ссылке {url}',
        settings.EMAIL_HOST_USER,
        [user.email]
    )
