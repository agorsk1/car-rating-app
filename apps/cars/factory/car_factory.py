import factory

from ..models import Car


class CarFactory(factory.django.DjangoModelFactory):
    """
    Car factory for testing purposes

    default values:
    car_model - golf 1, golf 2 etc. (Sequence)
    car_make - Volkswagen
    """
    class Meta:
        model = Car

    car_model = factory.Sequence(lambda n: f'Golf {n}')
    car_make = 'Volkswagen'
