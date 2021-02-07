from abc import ABC, abstractmethod

from django.test import TestCase

from rest_framework.generics import GenericAPIView
from rest_framework.test import APIRequestFactory

from apps.cars.factory import UserFactory


class AbstractBaseTest(object):
    class AbstractBaseApiTestCase(TestCase, ABC):
        """
        Abstract Base TestCase class.
        """
        def setUp(self) -> None:
            """Base setup"""
            self.user = UserFactory.create()
            self.request_factory = APIRequestFactory()
            self.view = self._view()
            self.endpoint = self._endpoint()

        @abstractmethod
        def _view(self) -> GenericAPIView.as_view():
            """Abstract method that returns YourApiToTest.as_view()"""
            pass

        @abstractmethod
        def _endpoint(self) -> str:
            """Abstract method that return endpoint string E.g /cars/"""
            pass

        @abstractmethod
        def test_anonymous_request(self, *args, **kwargs) -> None:
            """test if anonymous user cannot access endpoint"""
            pass
