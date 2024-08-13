# import factory
# from factory.django import DjangoModelFactory
#
# from items.models import Advertisement, Review
# from users.models import User
#
#
# class UserFactory(DjangoModelFactory):
#     class Meta:
#         model = User
#
#     email = factory.Faker('email')
#     password = factory.PostGenerationMethodCall('set_password', 'password')
#
#
# class AdvertisementFactory(DjangoModelFactory):
#     class Meta:
#         model = Advertisement
#
#     title = factory.Faker('sentence', nb_words=4)
#     author = factory.SubFactory(UserFactory)
#     price = factory.Faker('random_int', min=100, max=10000)
#     description = factory.Faker('text', max_nb_chars=200)
#     created_at = factory.Faker('date_time_this_year')
#
#
# class ReviewFactory(DjangoModelFactory):
#     class Meta:
#         model = Review
#
#     text = factory.Faker('text', max_nb_chars=200)
#     author = factory.SubFactory(UserFactory)
#     ad = factory.SubFactory(AdvertisementFactory)
#     created_at = factory.Faker('date_time_this_year')
