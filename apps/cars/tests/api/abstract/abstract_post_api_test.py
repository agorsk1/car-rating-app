from abc import ABC

from django.http import HttpResponse

from rest_framework.test import force_authenticate

from .abstract_base_api_test import AbstractBaseTest


class AbstractPostApiTest(object):
    """Class to avoid run the abstract class below"""
    class AbstractGetApiTestCase(AbstractBaseTest.AbstractBaseApiTestCase, ABC):
        """
        Abstract Post TestCase class.

        By default it checks if endpoint cannot be accessed by anonymous user.
        To use it please declare _get_view and _get_endpoint
        """
        def post_response(self, body: dict) -> HttpResponse:
            """Helper function that return response form /cars/ endpoint with authenticated user"""
            request = self.request_factory.post(self.endpoint, body)
            force_authenticate(request=request, user=self.user)
            response = self.view(request)
            return response

        def test_anonymous_request(self) -> None:
            """test if anonymous user cannot access endpoint with post request"""
            request = self.request_factory.post(self.endpoint)
            response = self.view(request)
            self.assertEqual(response.status_code, 403)
