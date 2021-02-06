from abc import ABC

from django.http import HttpResponse

from rest_framework.test import force_authenticate

from .abstract_base_api_test import AbstractBaseTest


class AbstractGetApiTest(object):
    """Class to avoid run the abstract class below"""
    class AbstractGetApiTestCase(AbstractBaseTest.AbstractBaseApiTestCase, ABC):
        """
        Abstract Get TestCase class.

        By default it checks if endpoint cannot be accessed by anonymous user.
        To use it please declare _get_view and _get_endpoint
        """
        def get_response(self) -> HttpResponse:
            """Helper function that return response from get endpoint with authenticated user"""
            request = self.request_factory.get(self.endpoint)
            force_authenticate(request=request, user=self.user)
            response = self.view(request)
            return response

        def test_anonymous_request(self) -> None:
            """test if anonymous user cannot access endpoint with get request"""
            request = self.request_factory.get(self.endpoint)
            response = self.view(request)
            self.assertEqual(response.status_code, 403)
