from django.db.models import QuerySet, Count

from ..models import Car


def get_all_cars_popularity() -> QuerySet():
    queryset = Car.objects.prefetch_related('car_rating') \
        .annotate(car_popularity=Count('car_rating'))
    return queryset
