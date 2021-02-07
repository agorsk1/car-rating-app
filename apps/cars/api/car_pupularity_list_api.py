from rest_framework.generics import ListAPIView

from ..selectors import get_all_cars_popularity
from .serializers import CarPopularitySerializer


class CarPopularityApi(ListAPIView):
    """
    Api that allows to get cars by popularity

    id - ID
    car_popularity - Count of ratings a
    car_make - Make of a car
    car_model - Model of a car
    """
    queryset = get_all_cars_popularity().order_by('-car_popularity')
    serializer_class = CarPopularitySerializer
