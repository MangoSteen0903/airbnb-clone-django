from django.db import models
from common.models import CommonModel


class Experience(CommonModel):

    """Definition of Experience Model"""

    country = models.CharField(
        max_length=50,
        default="South Korea",
    )
    city = models.CharField(
        max_length=80,
        default="Seoul",
    )

    name = models.CharField(max_length=250)
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="experiences",
    )
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    description = models.TextField()
    start = models.TimeField()
    end = models.TimeField()

    perks = models.ManyToManyField(
        "experiences.Perk",
        related_name="experiences",
    )

    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name


class Perk(CommonModel):
    """What is included on a Experience"""

    name = models.CharField(max_length=100)
    detail = models.CharField(
        max_length=250,
        blank=True,
        default="",
    )
    explanation = models.TextField(
        blank=True,
        default="",
    )

    def __str__(self):
        return self.name
