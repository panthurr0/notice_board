import pytest
from rest_framework.test import APIClient

from items.models import Advertisement
from users.models import User


@pytest.fixture
def user():
    return User.objects.create(email="testik@materials.py")


@pytest.fixture
def api_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def advertisement(user):
    return Advertisement.objects.create(title="Кресло", price=150, author=user)


@pytest.fixture
def review(user):
    return Advertisement.objects.create(text="Кресло понравилось!", ad=1, author=user)
