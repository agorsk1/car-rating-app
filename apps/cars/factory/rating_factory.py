import factory

from . import UserFactory, CarFactory
from ..models import Rating


class RatingFactory(factory.django.DjangoModelFactory):
    """
    Rating factory for testing purposes

    default values:
    rating_user - UserFactory (SubFactory)
    rating_stars - Rating.STAR_ONE, Rating.STAR_TWO (Iterator)
    rating_car - CarFactory (SubFactory)
    """
    class Meta:
        model = Rating

    rating_user = factory.SubFactory(UserFactory)
    rating_stars = factory.Iterator(Rating.STAR_CHOICES, getter=lambda c: c[0])
    rating_car = factory.SubFactory(CarFactory)

