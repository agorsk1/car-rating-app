from django.http import HttpResponse

from rest_framework.generics import GenericAPIView

from .abstract import AbstractGetApiTest
from ...api import CarPopularityApi
from ...factory import CarFactory, RatingFactory


class CarPopularityListApiTest(AbstractGetApiTest.AbstractGetApiTestCase):
    """Test checks if api that return data about cars popularity"""
    def _endpoint(self) -> str:
        return '/popular/'

    def _view(self) -> GenericAPIView.as_view():
        return CarPopularityApi.as_view()

    @staticmethod
    def _get_response_results(response: HttpResponse) -> list:
        return response.data['results']

    def test_no_data(self) -> None:
        """test if endpoint returns empty result when the db is empty"""
        response = self.get_response()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self._get_response_results(response), [])

    def test_if_all_columns_returned(self) -> None:
        """Test if all columns are included"""
        CarFactory.create()
        test_columns = {'id', 'car_model', 'car_make', 'car_popularity'}
        response = self.get_response()
        self.returned_keys = set(self._get_response_results(response)[0].keys())
        self.assertEqual(test_columns, self.returned_keys)

    def test_car_without_rating(self) -> None:
        """test if endpoint return 0 when car doesn't have a rating"""
        CarFactory.create()
        response = self.get_response()
        popularity = self._get_response_results(response)
        self. assertEqual(popularity[0]['car_popularity'], 0)

    def test_car_with_rating(self) -> None:
        """test if endpoint return correct count when car have a rating"""
        RatingFactory.create()
        response = self.get_response()
        popularity = self._get_response_results(response)
        self.assertEqual(popularity[0]['car_popularity'], 1)

    def test_ordering(self) -> None:
        """Test if endpoint returns correct ordering (from most to least popular)"""
        car_no_rating = CarFactory.create()

        one_rating = RatingFactory.create()
        car_one_rating = one_rating.rating_car

        car_two_ratings = CarFactory.create()
        two_rating = RatingFactory.create_batch(2, rating_car=car_two_ratings)

        response = self.get_response()
        popularity = self._get_response_results(response)
        self.assertEqual(popularity[0]['id'], car_two_ratings.id)
        self.assertEqual(popularity[1]['id'], car_one_rating.id)
        self.assertEqual(popularity[2]['id'], car_no_rating.id)
