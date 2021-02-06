from statistics import mean

import factory

from django.test import TestCase

from ...factory import CarFactory, RatingFactory
from ...models import Rating
from ...selectors.get_all_cars_with_avg_ratings import get_all_cars_with_avg_rating


class GetAllCarsWithAvgRatingSelectorTest(TestCase):
    """
    Test checks if all cars are correctly fetched from db and average ratings are correctly calculated
    """

    def test_empty_database(self) -> None:
        """Test if function returns empty queryset, when db is empty"""
        car_with_ratings = get_all_cars_with_avg_rating()
        self.assertFalse(car_with_ratings.exists())

    def test_if_there_is_a_car_and_no_ratings(self) -> None:
        """Test if there is no rating assign query returns 0"""
        CarFactory.create()
        car_with_ratings = get_all_cars_with_avg_rating().values('car_avg_rating')
        self.assertEqual(car_with_ratings[0]['car_avg_rating'], 0)

    def test_multiple_ratings_for_single_car(self) -> None:
        """Test if there are 2 ratings for a single car the mean rating value is calculated correctly"""
        car = CarFactory.create()
        ratings = [Rating.STAR_THREE, Rating.STAR_TWO]
        RatingFactory.create_batch(2,
                                   rating_car=car,
                                   rating_stars=factory.Iterator(ratings))
        car_with_ratings = get_all_cars_with_avg_rating().values('car_avg_rating')
        self.assertEqual(car_with_ratings[0]['car_avg_rating'], mean(ratings))

    def test_returned_items_for_multiple_cars(self) -> None:
        """
        Test if there are: car with no rating and 2 cars with ratings,
        all cars are returned correctly by the function
        """
        CarFactory.create()
        RatingFactory.create_batch(2)
        car_with_ratings = get_all_cars_with_avg_rating().values('car_model', 'car_avg_rating')
        self.assertEqual(len(car_with_ratings), 3)

    def test_number_of_queries(self):
        """
        Test if function executes exactly 1 queries:
        """
        RatingFactory.create_batch(2)
        with self.assertNumQueries(1):
            """force the execution"""
            list(get_all_cars_with_avg_rating().values('car_avg_rating', 'id', 'car_model'))
