import random
import string

from django.core.mail import send_mail

from config.settings import DEFAULT_FROM_EMAIL


def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = "".join(random.choice(characters) for _ in range(length))
    return password


def send_email(uid, token, email):
    send_mail(
        subject="Сброс пароля",
        message=f"Эндпоинт для подтверждения: /users/reset_password_confirm/\n"
        f"Укажите ваш uid: {uid}, ваш token: {token}\n"
        f"А также ваш new_password",
        from_email=DEFAULT_FROM_EMAIL,
        recipient_list=[email],
    )
