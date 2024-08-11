from rest_framework.generics import ListAPIView

from items.models import Advertisement


class AdvertisementListApiView(ListAPIView):
    """Выводит список объявлений"""

    queryset = Advertisement.objects.all()
    serializer_class = HabitSerializer