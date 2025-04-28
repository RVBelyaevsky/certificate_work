from rest_framework import status
from rest_framework.test import APITestCase


class UserTestCase(APITestCase):
    def setUp(self):
        pass

    def test_user_create(self):
        response = self.client.post(
            "/users/create/",
            data={
                "email": "test@example.com",
                "first_name": "test",
                "last_name": "test",
                "password": "user",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
