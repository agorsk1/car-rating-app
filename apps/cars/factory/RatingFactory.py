import factory

from ..models import Rating


class RatingFactory(factory.django.DjangoModelFactory):
    """
    Rating factory for testing purposes

    default values:
    None
    """
    class Meta:
        model = Rating
