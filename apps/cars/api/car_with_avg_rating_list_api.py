from rest_framework.generics import ListAPIView

from ..selectors import get_all_cars_with_avg_rating
from .serializers import CarWithAvgRatingSerializer


class CarWithAvgRatingListApi(ListAPIView):
    """
    The api that returns information about car's:

    id - ID
    car_avg_rating - Average car rating, if there is no rating this value equals 0
    car_make - Make of a car
    car_model - Model of a car
    """
    queryset = get_all_cars_with_avg_rating()
    serializer_class = CarWithAvgRatingSerializer
