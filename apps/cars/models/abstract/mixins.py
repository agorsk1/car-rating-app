from django.db import models
from django.utils.translation import gettext_lazy as _


class CreatedTimeStampMixin(models.Model):
    """Time Stamp mixin for tracking creation date and time of a data"""
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        verbose_name=_('Created at'),
        auto_now_add=True,
        editable=False
    )


class FullTimeStampMixin(CreatedTimeStampMixin):
    """Time Stamp mixin for tracking creation and last modification of a data"""
    class Meta:
        abstract = True

    updated_at = models.DateTimeField(
        verbose_name=_('Updated at'),
        auto_now=True,
        editable=False
    )
