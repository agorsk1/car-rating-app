from abc import ABC, abstractmethod

from django.http import HttpResponse
from django.test import TestCase

from rest_framework.generics import GenericAPIView
from rest_framework.test import APIRequestFactory, force_authenticate

from ....factory import UserFactory


class AbstractGetApiTest(object):
    """Class to avoid run the abstract class below"""
    class AbstractGetApiTestCase(TestCase, ABC):
        """
        Abstract TestCase class.

        By default it checks if endpoint cannot be accessed by anonymous user.
        To use it please declare _get_view and _get_endpoint
        """

        def setUp(self) -> None:
            """setup that creates test user and request factory and the view that we want to test"""
            self.user = UserFactory.create()
            self.request_factory = APIRequestFactory()
            self.view = self._get_view()
            self.endpoint = self._get_endpoint()

        @abstractmethod
        def _get_view(self) -> GenericAPIView.as_view():
            """Abstract method that returns YourApiToTest.as_view()"""
            pass

        @abstractmethod
        def _get_endpoint(self) -> str:
            """Abstract method that return endpoint string E.g /cars/"""
            pass

        def get_response(self) -> HttpResponse:
            """Helper function that return response form /cars/ endpoint with authenticated user"""
            request = self.request_factory.get(self.endpoint)
            force_authenticate(request=request, user=self.user)
            response = self.view(request)
            return response

        def test_anonymous_request(self) -> None:
            """test if anonymous user cannot access endpoint"""
            request = self.request_factory.get(self.endpoint)
            response = self.view(request)
            self.assertEqual(response.status_code, 403)
