from django.urls import path

from items.apps import ItemsConfig
from items.views import AdvertisementDestroyApiView, AdvertisementUpdateApiView, AdvertisementRetrieveApiView, \
    AdvertisementListApiView, AdvertisementCreateApiView, ReviewCreateApiView, ReviewListApiView, ReviewUpdateApiView, \
    ReviewDestroyApiView

app_name = ItemsConfig.name

urlpatterns = [
    # advertisements
    path("ads/create", AdvertisementCreateApiView.as_view(), name="advertisement-create"),
    path("ads/", AdvertisementListApiView.as_view(), name="advertisement-list"),
    path("ads/<int:pk>", AdvertisementRetrieveApiView.as_view(), name="advertisement-detail"),
    path("ads/update/<int:pk>", AdvertisementUpdateApiView.as_view(), name="advertisement-update"),
    path(
        "ads/delete/<int:pk>", AdvertisementDestroyApiView.as_view(), name="advertisement-delete"
    ),
    
    # reviews
    path("review/create", ReviewCreateApiView.as_view(), name="review-create"),
    path("review/", ReviewListApiView.as_view(), name="review-list"),
    path("review/update/<int:pk>", ReviewUpdateApiView.as_view(), name="review-update"),
    path(
        "review/delete/<int:pk>", ReviewDestroyApiView.as_view(), name="review-delete"
    ),
]
