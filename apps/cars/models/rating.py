from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from .abstract.mixins import FullTimeStampMixin
from .car import Car


class Rating(FullTimeStampMixin):
    """
    Rating Model that is extension of FullTimeStamp Mixing. Rating stores information about users' car ratings.

    Single user can add only one rating of a specific car.
    """
    class Meta:
        verbose_name = _('Car rating')
        verbose_name_plural = _('Car ratings')
        unique_together = ['rating_user', 'rating_car']

    STAR_ONE = 1
    STAR_TWO = 2
    STAR_THREE = 3
    STAR_FOUR = 4
    STAR_FIVE = 5
    STAR_CHOICES = (
        (STAR_ONE, 1),
        (STAR_TWO, 2),
        (STAR_THREE, 3),
        (STAR_FOUR, 4),
        (STAR_FIVE, 5)
    )

    rating_user = models.ForeignKey(
        get_user_model(),
        verbose_name=_('User'),
        related_name='car_rating',
        on_delete=models.CASCADE,
        help_text=_('User that rated a car')
    )
    rating_stars = models.PositiveSmallIntegerField(
        verbose_name=_('Stars'),
        choices=STAR_CHOICES,
        help_text=_('Rating of a car from 1 to 5')
    )
    rating_car = models.ForeignKey(
        Car,
        verbose_name=_('Car'),
        related_name='car_rating',
        on_delete=models.CASCADE,
        help_text=_('Car model that is rated by a user')
    )

    def __str__(self) -> str:
        return f'{self.rating_stars} for {self.rating_car} by {self.rating_user}'
