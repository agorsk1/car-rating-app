from decimal import Decimal
from statistics import mean

import factory
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView

from .abstract.abstract_get_api_test import AbstractGetApiTest
from ...api import CarListCreateApi
from ...factory import CarFactory, RatingFactory
from ...models import Rating


class CarWithAvgRatingListApiTest(AbstractGetApiTest.AbstractGetApiTestCase):
    """
    Test checks if api that return data about cars and its star ratings works correctly
    """
    def _endpoint(self) -> str:
        return '/cars/'

    def _view(self) -> GenericAPIView.as_view():
        return CarListCreateApi.as_view()

    @staticmethod
    def _get_response_results(response: HttpResponse) -> list:
        return response.data['results']

    def test_no_data(self) -> None:
        """test if endpoint returns empty result when the db is empty"""
        response = self.get_response()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self._get_response_results(response), [])

    def test_if_all_columns_are_returned(self) -> None:
        """Test if endpoint returns all columns correctly"""
        test_keys = {'id', 'car_make', 'car_model', 'car_avg_rating'}
        CarFactory.create()
        response = self.get_response()
        returned_keys = set(self._get_response_results(response)[0].keys())
        self.assertEqual(test_keys, returned_keys)

    def test_car_without_rating(self) -> None:
        """test if endpoint returns 0 when car doesn't have a rating"""
        CarFactory.create()
        response = self.get_response()
        returned_avg_value = self._get_response_results(response)[0]['car_avg_rating']
        self.assertEqual(Decimal(returned_avg_value), Decimal('0.00'))

    def test_single_car_with_ratings(self) -> None:
        """test if endpoint returns correct avg value for multiple values"""
        car = CarFactory.create()
        ratings = [Rating.STAR_THREE, Rating.STAR_TWO]
        RatingFactory.create_batch(2,
                                   rating_car=car,
                                   rating_stars=factory.Iterator(ratings))
        response = self.get_response()
        returned_avg_value = self._get_response_results(response)[0]['car_avg_rating']
        self.assertEqual(Decimal(returned_avg_value), Decimal(mean(ratings)))
