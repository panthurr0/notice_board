import pytest
from django.urls import reverse
from rest_framework import status

from items.models import Advertisement


@pytest.mark.django_db
def test_advertisement_create(api_client):
    """Тестирование создания объявления."""
    url = reverse("items:advertisement-create")
    data = {"title": "Стул", "price": 120}
    response = api_client.post(url, data)

    assert response.status_code == status.HTTP_201_CREATED
    assert Advertisement.objects.count() == 1


@pytest.mark.django_db
def test_advertisement_list(api_client):
    """Тестирование списка объявлений."""
    url = reverse("items:advertisement-list")
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_advertisement_retrieve(api_client, advertisement):
    """Тестирование просмотра объявления."""
    url = reverse("items:advertisement-detail", args=(advertisement.pk,))
    response = api_client.get(url)
    data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert data.get("title") == advertisement.title


@pytest.mark.django_db
def test_advertisement_update(api_client, advertisement):
    """Тестирование редактирования объявления."""
    url = reverse("items:advertisement-update", args=(advertisement.pk,))
    data = {"price": "200"}
    response = api_client.patch(url, data)
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert response_data.get("price") == 200


@pytest.mark.django_db
def test_advertisement_delete(api_client, advertisement):
    """Тестирование удаления объявления."""
    url = reverse("items:advertisement-delete", args=(advertisement.pk,))
    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Advertisement.objects.count() == 0
