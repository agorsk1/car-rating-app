from typing import OrderedDict, Union, Dict

from rest_framework import serializers

from .models import Car
from .selectors import get_models_for_make


class CarSaveService:
    """Car service used for validation of the data during creation of a new car"""
    def __init__(self, data: OrderedDict[str, str]):
        self.data = data
        self.fetched_car_data = self._get_valid_car_models()
        self.valid_car_data = None

    def _get_valid_car_models(self) -> dict:
        """Method that returns data about car models for selected car make"""
        return get_models_for_make(self.data['car_make'])['Results']

    def _validate_car_make(self):
        """Check if valid_car_models are empty"""
        if not self.fetched_car_data:
            raise serializers.ValidationError(f'Make {self.data["car_make"]} does not exist')

    def _validate_car_model(self):
        """Check if car model exists"""
        self._search_valid_car()
        if not self.valid_car_data:
            raise serializers.ValidationError(f'Model {self.data["car_model"]} does not exist')

    def _search_valid_car(self) -> None:
        """Search function which assigns valid car data"""
        search_model = self.data['car_model'].upper()
        for car_data in self.fetched_car_data:
            x = car_data['Model_Name'].upper()
            if car_data['Model_Name'].upper() == search_model:
                self.valid_car_data = car_data
                break

    def _validate_car_exists(self):
        """Check if car already exists in the db"""
        if Car.objects.filter(**self.get_normalized_data()).exists():
            raise serializers.ValidationError('The fields car_make, car_model must make a unique set.')

    def validate_data(self):
        """Validate the data. Please do not change the order"""
        self._validate_car_make()
        self._validate_car_model()
        self._validate_car_exists()

    def get_normalized_data(self) -> Dict[str, str]:
        """Return normalized data received from external source"""
        return {
            'car_make': self.valid_car_data['Make_Name'],
            'car_model': self.valid_car_data['Model_Name']
        }

