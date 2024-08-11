from rest_framework.serializers import ModelSerializer

from items.models import Advertisement, Review


class AdvertisementSerializer(ModelSerializer):
    class Meta:
        model = Advertisement
        fields = "__all__"


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
