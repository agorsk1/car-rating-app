from typing import List
from unittest.mock import patch

from rest_framework.generics import GenericAPIView

from .abstract import AbstractPostApiTest
from ...api import CarListCreateApi
from ...factory import CarFactory
from ...service import CarSaveService


@patch.object(CarSaveService, '_get_valid_car_models')
class CarCreateApiTest(AbstractPostApiTest.AbstractGetApiTestCase):
    def _endpoint(self) -> str:
        return '/cars/'

    def _view(self) -> GenericAPIView.as_view():
        return CarListCreateApi.as_view()

    @staticmethod
    def _mock_valid_data() -> List[dict]:
        valid_car_list = []
        for car in CarFactory.build_batch(2, car_make='Volkswagen'):
            valid_car_list.append({
                'Make_Name': car.car_make,
                'Model_Name': car.car_model})
        return valid_car_list

    def _body(self, mock_data, car_make: str = None, car_model: str = None) -> dict:
        if not car_make:
            car_make = mock_data[0]['Make_Name']
        if not car_model:
            car_model = mock_data[0]['Model_Name']
        return {
            'car_make': car_make,
            'car_model': car_model
        }

    def test_no_data(self, mock_fetched_data) -> None:
        """test if client send empty body, endpoint will return 400"""
        mock_fetched_data.return_value = []
        response = self.post_response(body={})
        self.assertEqual(response.status_code, 400)

    def test_wrong_car_make(self, mock_fetched_data) -> None:
        """Test if endpoint return 400 for wrong car make"""
        mock_data = self._mock_valid_data()
        mock_fetched_data.return_value = []
        response = self.post_response(body=self._body(mock_data, car_make='chomik'))
        self.assertEqual(response.status_code, 400)

    def test_wrong_car_model(self, mock_fetched_data) -> None:
        """Test if endpoint return 400 for wrong car model"""
        mock_data = self._mock_valid_data()
        mock_fetched_data.return_value = mock_data
        response = self.post_response(body=self._body(mock_data, car_model='chomik'))
        self.assertEqual(response.status_code, 400)

    def test_correct_data(self, mock_fetched_data) -> None:
        """Test valid data"""
        mock_data = self._mock_valid_data()
        mock_fetched_data.return_value = mock_data
        response = self.post_response(body=self._body(mock_data))
        self.assertEqual(response.status_code, 201)

    def test_correct_data_upper(self, mock_fetched_data) -> None:
        """Test valid data but in uppercase"""
        mock_data = self._mock_valid_data()
        mock_fetched_data.return_value = mock_data
        body = self._body(mock_data)
        for key in body.keys():
            body[key] = body[key].upper()
        response = self.post_response(body=body)
        self.assertEqual(response.status_code, 201)

    def test_car_exists(self, mock_fetched_data) -> None:
        """Test if endpoint returns 400 for car that already exists"""
        mock_data = self._mock_valid_data()
        mock_fetched_data.return_value = mock_data
        body = self._body(mock_data)
        CarFactory.create(**body)
        response = self.post_response(body=body)
        self.assertEqual(response.status_code, 400)
