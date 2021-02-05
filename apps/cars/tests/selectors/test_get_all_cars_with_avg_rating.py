from django.test import TestCase

from ...factory import CarFactory, RatingFactory, UserFactory
from ...models import Rating
from ...selectors.get_all_cars_with_avg_ratings import get_all_cars_with_avg_rating


class GetAllCarsWithAvgRatingSelectorTest(TestCase):
    """
    Test checks if all cars are correctly fetched from db and average ratings are correctly calculated
    """

    def test_empty_database(self) -> None:
        """Test if function returns empty list if db is empty"""
        car_with_ratings = get_all_cars_with_avg_rating()
        self.assertEqual(car_with_ratings, [])

    def test_if_there_is_a_car_and_no_ratings(self) -> None:
        """Test if there is no rating assign query returns 0"""
        CarFactory.create()
        car_with_ratings = get_all_cars_with_avg_rating()
        self.assertEqual(car_with_ratings[0]['avg_rating'], 0)

    def test_if_there_are_multiple_ratings(self) -> None:
        """Test if there are 2 ratings for a single car"""
        car = CarFactory.create()
        users = UserFactory.create_batch(2)
        ratings = [Rating.STAR_THREE, Rating.STAR_TWO]
        for user, rating in zip(users, ratings):
            RatingFactory.create(rating_user=user, rating_car=car, rating_star=rating)
        car_with_ratings = get_all_cars_with_avg_rating()
        self.assertEqual(car_with_ratings[0]['avg_rating'], 2.50)

# TODO: Add test for count of returned elements from the function
# TODO: Add test for if multiple ratings return correct avg rating value
