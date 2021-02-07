from rest_framework.generics import ListAPIView


class CarPopularityApi(ListAPIView):
    """
    Api that allows to get cars by popularity

    id - ID
    car_popularity - Count of ratings a
    car_make - Make of a car
    car_model - Model of a car
    """
    pass
