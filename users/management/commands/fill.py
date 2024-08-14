import json
import pathlib

from django.core.management import BaseCommand
from django.db import connection

from items.models import Advertisement, Review
from users.models import User

ROOT = pathlib.Path(__file__).parent.parent.parent.parent
DATA_ADS = pathlib.Path(ROOT, 'json_data', 'advertisements.json')
DATA_REVIEWS = pathlib.Path(ROOT, 'json_data', 'reviews.json')


class Command(BaseCommand):

    @staticmethod
    def json_read(path) -> list:
        # Здесь мы получаем данные из фикстур
        with open(path) as file:
            file_info = json.load(file)
        return [info for info in file_info]

    def handle(self, *args, **options):
        # Очистка базы данных перед заполнением
        Advertisement.objects.all().delete()
        Review.objects.all().delete()

        advertisement_for_create = []
        review_for_create = []

        with connection.cursor() as cursor:
            cursor.execute(
                "TRUNCATE TABLE items_advertisement, items_review "
                "RESTART IDENTITY CASCADE;")

        for ad in Command.json_read(DATA_ADS):
            ads_field = ad.get('fields')
            advertisement_for_create.append(
                Advertisement(title=ads_field.get('title'),
                              author=User.objects.get(pk=ads_field.get('author')),
                              price=ads_field.get('price'),
                              description=ads_field.get('description'))
            )

        Advertisement.objects.bulk_create(advertisement_for_create)

        for review in Command.json_read(DATA_REVIEWS):
            review_field = review.get('fields')
            review_for_create.append(
                Review(text=review_field.get('text'),
                       author=User.objects.get(pk=review_field.get('author')),
                       ad=Advertisement.objects.get(pk=review_field.get('ad'))
                       )
            )

        Review.objects.bulk_create(review_for_create)
