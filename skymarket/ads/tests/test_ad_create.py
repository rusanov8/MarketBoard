from rest_framework import status
from rest_framework.test import APITestCase
import json

from users.models import User
from ads.models import Ad


class TestAdCreation(APITestCase):
    """
        Test cases for creating ad using the AdViewSet API endpoint.
    """

    def setUp(self):
        """
        Set up data for each test case.
        """
        self.user = User.objects.create_user(
            email='ivanov@mail.ru',
            first_name='Ivan',
            last_name='Ivanov',
            phone='+79000000000',
            role='user',
            image=None
        )

        self.client.force_authenticate(user=self.user)

        self.ad_data = {
            'title': 'Test Ad',
            'price': 1,
            'description': 'Test Ad',
            'author': self.user,
        }

    def test_create_ad(self):

        response = self.client.post('/api/ads/', self.ad_data,)

        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Ad.objects.all().exists())
        self.assertEqual(response_data['title'], self.ad_data['title'])


