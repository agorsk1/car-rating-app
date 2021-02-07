from rest_framework.generics import ListCreateAPIView

from ..selectors import get_all_cars_with_avg_rating
from .serializers import CarSerializer


class CarListCreateApi(ListCreateAPIView):
    """
    The api that is responsible for listing cars and avg rating of them and new car creation

    GET:
    id - ID
    car_avg_rating - Average car rating, if there is no rating this value equals 0
    car_make - Make of a car
    car_model - Model of a car

    POST:
    car_make - Make of a car
    car_model - Model of a car
    """
    queryset = get_all_cars_with_avg_rating()
    serializer_class = CarSerializer
