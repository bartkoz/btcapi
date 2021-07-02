from unittest import mock

from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APIClient

from api.models import EntryPoint
from api.tasks import fetch_data

mock_response = {
    "Realtime Currency Exchange Rate": {
        "1. From_Currency Code": "BTC",
        "2. From_Currency Name": "Bitcoin",
        "3. To_Currency Code": "CNY",
        "4. To_Currency Name": "Chinese Yuan",
        "5. Exchange Rate": "214232.06479500",
        "6. Last Refreshed": "2021-07-02 13:03:09",
        "7. Time Zone": "UTC",
        "8. Bid Price": "214212.53415300",
        "9. Ask Price": "214235.42768700",
    }
}


class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_no_token(self):
        r = self.client.get(reverse("api:quotes"))
        self.assertEqual(r.status_code, 403)

    def test_get_with_token(self):
        with self.settings(API_KEY="test"):
            r = self.client.get(reverse("api:quotes"), {"api_key": "test"})
            self.assertEqual(r.status_code, 200)

    def test_post_no_token(self):
        r = self.client.get(reverse("api:quotes"))
        self.assertEqual(r.status_code, 403)

    @mock.patch('api.tasks.fetch_data')
    def test_post_with_token(self, mock_fetch):
        with self.settings(API_KEY="test"):
            r = self.client.post('/api/v1/quotes?api_key=test', follow=True)
            self.assertEqual(r.status_code, 200)


class TaskTests(TestCase):
    @mock.patch('requests.get')
    def test_fetch_data(self, mock_resp):
        mock_resp.return_value.json.return_value = mock_response
        fetch_data()
        self.assertEqual(EntryPoint.objects.count(), 1)
