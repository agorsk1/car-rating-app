from decimal import Decimal

from django.db.models import QuerySet, Avg
from django.db.models.functions import Coalesce

from ..models import Car


def get_all_cars_with_avg_rating() -> QuerySet():
    queryset = Car.objects.prefetch_related('car_rating')\
        .annotate(car_avg_rating=Coalesce(Avg('car_rating__rating_stars'), Decimal(0.0)))
    return queryset
