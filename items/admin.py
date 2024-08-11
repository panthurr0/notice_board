from django.contrib import admin

from items.models import Advertisement, Review


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author")
    list_filter = ("id", "author")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "created_at")
    list_filter = ("id", "author")
