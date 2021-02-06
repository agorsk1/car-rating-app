from rest_framework.generics import CreateAPIView

from apps.cars.api.serializers.rating_serializer import RatingSerializer
from apps.cars.models import Rating


class RatingPostApi(CreateAPIView):
    """Api that allows to rate a car"""
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

