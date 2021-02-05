from django.db import models
from django.utils.translation import gettext_lazy as _

from .abstract.mixins import TimeStampMixin


class Car(TimeStampMixin):
    """
    Car model that is an extension of TimeStamp Model mixing. It stores information about car model and make
    """
    class Meta:
        verbose_name = _('Car')
        verbose_name_plural = _('Cars')

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
