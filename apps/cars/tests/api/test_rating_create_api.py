from rest_framework.generics import GenericAPIView

from .abstract import AbstractPostApiTest
from ...api.rating_create_api import RatingCreateApi
from ...factory import CarFactory
from ...models import Rating


class RatingPostApiTest(AbstractPostApiTest.AbstractGetApiTestCase):
    def _endpoint(self) -> str:
        return '/rate/'

    def _view(self) -> GenericAPIView.as_view():
        return RatingCreateApi.as_view()

    def test_no_data(self) -> None:
        """test if client send empty body, endpoint will return 400"""
        response = self.post_response(body={})
        self.assertEqual(response.status_code, 400)

    def test_wrong_car_data(self) -> None:
        """test if client send wrong rating car, endpoint will return 400"""
        response = self.post_response(body={
            'rating_car': -1,
            'rating_stars': Rating.STAR_TWO
        })
        self.assertEqual(response.status_code, 400)

    def test_wrong_rating_star(self) -> None:
        """test if client send wrong rating star, endpoint will return 400"""
        car = CarFactory.create()
        response = self.post_response(body={
            'rating_car': car.id,
            'rating_stars': -10
        })
        self.assertEqual(response.status_code, 400)

    def test_extra_key_added(self) -> None:
        """test if client send extra key, endpoint will return 201"""
        car = CarFactory.create()
        response = self.post_response(body={
            'rating_car': car.id,
            'rating_stars': Rating.STAR_TWO,
            'kamil stoch': 'dawid kubacki'
        })
        self.assertEqual(response.status_code, 201)

    def test_add_rating(self) -> None:
        """test if client send good data, everything will be saved correctly"""
        car = CarFactory.create()
        body = {
            'rating_car': car.id,
            'rating_stars': Rating.STAR_TWO
        }
        response = self.post_response(body=body)
        rating = Rating.objects.first()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(rating.rating_user_id, self.user.id)
        self.assertEqual(rating.rating_stars, response.data['rating_stars'])
        self.assertEqual(rating.rating_car_id, response.data['rating_car'])

    def test_duplicated_rating(self) -> None:
        """test if user rates 2 times the same car the endpoint will return 400"""
        car = CarFactory.create()
        body = {
            'rating_car': car.id,
            'rating_stars': Rating.STAR_TWO
        }
        response = self.post_response(body=body)
        self.assertEqual(response.status_code, 201)
        body['rating_stars'] = Rating.STAR_FOUR
        duplicated_data_response = self.post_response(body=body)
        self.assertEqual(duplicated_data_response.status_code, 400)
