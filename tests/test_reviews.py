import pytest
from django.urls import reverse
from rest_framework import status

from items.models import Review


@pytest.mark.django_db
def test_review_create(api_client):
    """Тестирование создания отзыва."""
    url = reverse("items:review-create")
    data = {"text": "Стул понравился!"}
    response = api_client.post(url, data)

    assert response.status_code == status.HTTP_201_CREATED
    assert Review.objects.count() == 1


@pytest.mark.django_db
def test_review_list(api_client):
    """Тестирование списка отзывов."""
    url = reverse("items:review-list")
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_review_update(api_client, review):
    """Тестирование редактирования отзыва."""
    url = reverse("items:review-update", args=(review.pk,))
    data = {"text": "Кресло понравилось!"}
    response = api_client.patch(url, data)
    response_data = response.json()
    print(response_data)
    assert response.status_code == status.HTTP_200_OK
    assert response_data.get("text") == "Кресло понравилось!"


@pytest.mark.django_db
def test_review_delete(api_client, review):
    """Тестирование удаления отзыва."""
    url = reverse("items:review-delete", args=(review.pk,))
    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Review.objects.count() == 0
