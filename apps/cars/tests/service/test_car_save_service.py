from collections import OrderedDict
from unittest.mock import patch

from django.test import TestCase
from rest_framework import serializers

from ...factory import CarFactory
from ...service import CarSaveService


@patch.object(CarSaveService, '_get_valid_car_models')
class CarSaveServiceTest(TestCase):
    """
    Car save service test with mocked method _get_valid_car_models which normally
    calls external service
    """
    def setUp(self) -> None:
        self.valid_car_list = []
        for car in CarFactory.build_batch(2, car_make='Volkswagen'):
            self.valid_car_list.append({
                'Make_Name': car.car_make,
                'Model_Name': car.car_model})

    def _data(self, car_make: str = None, car_model: str = None) -> OrderedDict[str, str]:
        if not car_make:
            car_make = self.valid_car_list[0]['Make_Name']
        if not car_model:
            car_model = self.valid_car_list[0]['Model_Name']
        return OrderedDict({
            'car_make': car_make,
            'car_model': car_model
        })

    @staticmethod
    def _run_service(data) -> dict:
        """Helper function that run the service"""
        service = CarSaveService(data)
        service.validate_data()
        return service.get_normalized_data()

    def test_valid_data(self, mock_fetched_data) -> None:
        """Test if user post valid data"""
        mock_fetched_data.return_value = self.valid_car_list
        data = self._data()
        validated_data = self._run_service(data)
        self.assertEqual(validated_data['car_make'], self.valid_car_list[0]['Make_Name'])
        self.assertEqual(validated_data['car_model'], self.valid_car_list[0]['Model_Name'])

    def test_invalid_make(self, mock_fetched_data) -> None:
        """Test if service raise ValidationError for invalid make"""
        mock_fetched_data.return_value = []
        data = self._data(car_make='chomik')
        with self.assertRaises(serializers.ValidationError):
            self._run_service(data)

    def test_invalid_model(self, mock_fetched_data) -> None:
        """Test if service raise ValidationError for invalid model"""
        mock_fetched_data.return_value = self.valid_car_list
        data = self._data(car_model='chomik')
        with self.assertRaises(serializers.ValidationError):
            self._run_service(data)

    def test_car_already_exist(self, mock_fetched_data) -> None:
        """Test if service raise ValidationError for a car that already exists"""
        mock_fetched_data.return_value = self.valid_car_list
        data = self._data()
        CarFactory.create(**data)
        with self.assertRaises(serializers.ValidationError):
            self._run_service(data)

    def test_num_of_queries(self, mock_fetched_data):
        """Test if there are not any extra queries"""
        mock_fetched_data.return_value = self.valid_car_list
        data = self._data()
        with self.assertNumQueries(1):
            self._run_service(data)
