from django.db import models
from django.utils.translation import gettext_lazy as _

from .abstract.mixins import CreatedTimeStampMixin


class Car(CreatedTimeStampMixin):
    """
    Car model that is an extension of CreatedTimeStamp Model mixing. It stores information about car model and make
    """
    class Meta:
        verbose_name = _('Car')
        verbose_name_plural = _('Cars')
        unique_together = ['car_make', 'car_model']

    car_make = models.CharField(
        verbose_name=_('Make'),
        max_length=255,
        help_text=_('Make of a car')
    )
    car_model = models.CharField(
        verbose_name=_('Model'),
        max_length=255,
        help_text=_('Model of a car')
    )

    def __str__(self) -> str:
        return f'{self.car_make} {self.car_model}'
