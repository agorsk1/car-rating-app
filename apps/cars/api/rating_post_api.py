from rest_framework.generics import CreateAPIView

from apps.cars.api.serializers.rating_serializers import RatingSerializer
from apps.cars.models import Rating


class RatingPostApi(CreateAPIView):
    """
    Api that allows to rate a car

    rating_car - id of car
    rating_stars - Value from Rating.STAR_CHOICES

    user is taken automatically from the request and a user cannot rate the same car 2 times
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
