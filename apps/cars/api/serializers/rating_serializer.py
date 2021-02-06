from rest_framework import serializers

from ...models import Rating


class RatingSerializer(serializers.ModelSerializer):
    """Rating model serializer"""
    rating_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Rating
        fields = '__all__'
