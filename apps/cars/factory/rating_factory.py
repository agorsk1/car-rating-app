import factory

from ..models import Rating


class SingleRatingFactory(factory.django.DjangoModelFactory):
    """
    Rating factory for testing purposes

    default values:
    None
    """
    class Meta:
        model = Rating

    rating_start = factory.Iterator(Rating.STAR_CHOICES, getter=lambda c: c[0])

