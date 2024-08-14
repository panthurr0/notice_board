import string
from unittest import mock

import pytest

from config.settings import DEFAULT_FROM_EMAIL
from users.services import generate_password, send_email


def test_generate_password():
    length = 10
    password = generate_password(length)
    allowed_characters = string.ascii_letters + string.digits

    assert len(password) == length
    assert all(char in allowed_characters for char in password)


@pytest.mark.django_db
@mock.patch("users.services.send_mail")
def test_send_email(mock_send_mail):
    uid = 123
    token = "testtoken"
    email = "testik@materials.py"

    send_email(uid, token, email)

    mock_send_mail.assert_called_once_with(
        subject="Сброс пароля",
        message=(
            "Эндпоинт для подтверждения: /users/reset_password_confirm/\n"
            f"Укажите ваш uid: {uid}, ваш token: {token}\n"
            "А также ваш new_password"
        ),
        from_email=DEFAULT_FROM_EMAIL,
        recipient_list=[email],
    )
