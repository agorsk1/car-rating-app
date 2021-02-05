from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from ..models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Rating admin panel settings"""
    list_display = ['rating_user', 'rating_stars', 'get_car_model', 'get_car_make']
    list_select_related = ['rating_car', 'rating_user']
    list_filter = ['created_at', 'updated_at', 'rating_user', 'rating_stars']
    search_fields = ['rating_user', 'rating_car__car_make', 'rating_car__car_model']
    ordering = ['rating_car__car_make', 'rating_car__car_model']

    def get_username(self, obj: Rating) -> str:
        return obj.rating_user.get_username()

    get_username.short_description = _('Username')
    get_username.admin_order_field = 'rating_user__username'

    def get_car_model(self, obj: Rating) -> str:
        return obj.rating_car.car_model

    get_car_model.short_description = _('Car model')
    get_car_model.admin_order_field = 'rating_car__car_model'

    def get_car_make(self, obj: Rating) -> str:
        return obj.rating_car.car_make

    get_car_make.short_description = _('Car make')
    get_car_make.admin_order_field = 'rating_car__car_make'
