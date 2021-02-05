from django.contrib import admin

from ..models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['car_make', 'car_model', 'created_at']
    list_filter = ['created_at', 'car_make']
    search_fields = ['car_make', 'car_model']
    ordering = ['car_make', 'car_model']
