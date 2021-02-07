from django.test import TestCase

from ...selectors import get_models_for_make


class GetModelsForMakeTest(TestCase):
    def test_external_service_online(self) -> None:
        result = get_models_for_make('honda')
        self.assertIn('Results', set(result.keys()))
