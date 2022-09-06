from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Fliter By Good & Bad Review"

    parameter_name = "positive"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("bad", "Bad"),
            ("mediocre", "Mediocre"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word == "good":
            return reviews.filter(rating__gt=3)
        elif word == "bad":
            return reviews.filter(rating__lt=3)
        elif word == "mediocre":
            return reviews.filter(rating__exact=3)
        else:
            return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
