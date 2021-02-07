from django.test import TestCase

from ...factory import CarFactory, RatingFactory
from ...selectors import get_all_cars_popularity


class GetAllCarsPopularityTest(TestCase):
    def test_empty_database(self) -> None:
        """Test if function returns empty queryset, when db is empty"""
        cars_popularity = get_all_cars_popularity()
        self.assertFalse(cars_popularity.exists())

    def test_no_rating(self) -> None:
        """Test if query returns 0 if car doesn't have a rating"""
        CarFactory.create()
        cars_popularity = get_all_cars_popularity().values('car_popularity', 'car_model')
        self.assertEqual(cars_popularity[0]['car_popularity'], 0)

    def test_with_rating(self) -> None:
        """Test if query returns correct count of ratings when there is one car and 2 ratings"""
        RatingFactory.create_batch(2, rating_car=CarFactory.create())
        cars_popularity = get_all_cars_popularity().values('car_popularity', 'car_model')
        self.assertEqual(cars_popularity[0]['car_popularity'], 2)

    def test_multiple_cars(self) -> None:
        """Test if query returns correct count for multiple cars and ratings"""
        RatingFactory.create_batch(2)
        cars_popularity = get_all_cars_popularity().values('car_popularity', 'car_model')
        for car in cars_popularity:
            self.assertEqual(car['car_popularity'], 1)

    def test_num_of_queries(self) -> None:
        """Test number of queries"""
        RatingFactory.create_batch(3)
        with self.assertNumQueries(1):
            list(get_all_cars_popularity().values('car_popularity', 'car_model'))
