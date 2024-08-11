from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from items.models import Advertisement, Review
from items.paginators import AdvertisementPaginator
from items.serializers import AdvertisementSerializer, ReviewSerializer
from users.permissions import IsAdmin, IsAuthor


class AdvertisementCreateApiView(CreateAPIView):
    serializer_class = AdvertisementSerializer

    def perform_create(self, serializer):
        """
        Привязывает к текущему пользователю
        """
        u = self.request.user
        serializer.save(author=u)


class AdvertisementListApiView(ListAPIView):
    """Выводит список всех объявлений"""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (AllowAny,)
    pagination_class = AdvertisementPaginator

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('title',)


class AdvertisementRetrieveApiView(RetrieveAPIView):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()


class AdvertisementUpdateApiView(UpdateAPIView):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()
    permission_classes = [IsAdmin | IsAuthor]


class AdvertisementDestroyApiView(DestroyAPIView):
    queryset = Advertisement.objects.all()
    permission_classes = [IsAdmin | IsAuthor]


class ReviewCreateApiView(CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        """
        Привязывает к текущему пользователю
        """
        u = self.request.user
        serializer.save(author=u)


class ReviewListApiView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewUpdateApiView(UpdateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAdmin | IsAuthor]


class ReviewDestroyApiView(DestroyAPIView):
    queryset = Review.objects.all()
    permission_classes = [IsAdmin | IsAuthor]
