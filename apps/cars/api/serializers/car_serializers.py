from rest_framework import serializers

from django.utils.translation import gettext_lazy as _

from ...models import Car


class CarWithAvgRatingSerializer(serializers.ModelSerializer):
    """Car model serializer that also accepts avg ratings for each car"""
    car_avg_rating = serializers.DecimalField(
        label=_('Car average rating'),
        max_digits=3,
        decimal_places=2,
        read_only=True,
        help_text=_('Average car rating, if there is no rating this value equals 0')
    )

    class Meta:
        model = Car
        exclude = ['created_at']


class CarPopularitySerializer(serializers.ModelSerializer):
    """Car model serializer that also accepts car popularity"""
    car_popularity = serializers.IntegerField(
        label=_('Car popularity'),
        read_only=True,
        help_text=_('Count of ratings of a car')
    )

    class Meta:
        model = Car
        exclude = ['created_at']
