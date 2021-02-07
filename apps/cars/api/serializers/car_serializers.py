from rest_framework import serializers

from django.utils.translation import gettext_lazy as _

from ...models import Car
from ...service import CarSaveService


class CarSerializer(serializers.ModelSerializer):
    """Car model serializer that also accepts avg ratings for each car"""
    car_avg_rating = serializers.DecimalField(
        label=_('Car average rating'),
        max_digits=3,
        decimal_places=2,
        read_only=True,
        help_text=_('Average car rating, if there is no rating this value equals 0')
    )

    def get_unique_together_validators(self):
        """
        Overriding method to disable unique together checks

        this validation is implemented as CarServiceValidator
        """
        return []

    def validate(self, data):
        car_service = CarSaveService(data)
        car_service.validate_data()
        return car_service.get_normalized_data()

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
